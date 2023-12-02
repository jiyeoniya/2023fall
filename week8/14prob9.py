import torch
import torch.nn.functional as F
from torch_geometric.datasets import Planetoid
import torch_geometric.transforms as T
from torch_geometric.nn import GCNConv
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 从PyTorch Geometric加载Cora数据集
dataset = Planetoid(root='data/Cora', name='Cora', transform=T.NormalizeFeatures())
data = dataset[0]

# 定义一个GCN模型
class GCN(torch.nn.Module):
    def __init__(self, num_features, hidden_channels, num_classes):
        super(GCN, self).__init__()
        self.conv1 = GCNConv(num_features, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, num_classes)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = F.relu(self.conv1(x, edge_index))
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

# 初始化模型
model = GCN(dataset.num_features, hidden_channels=16, num_classes=dataset.num_classes)

# 损失函数和优化器
criterion = torch.nn.NLLLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# 训练模型
model.train()
for epoch in range(200):
    optimizer.zero_grad()
    out = model(data)
    loss = criterion(out[data.train_mask], data.y[data.train_mask])
    loss.backward()
    optimizer.step()

# 评估模型
model.eval()
with torch.no_grad():
    logits = model(data)
    pred = logits.argmax(dim=1)
    acc = (pred[data.test_mask] == data.y[data.test_mask]).sum().item() / data.test_mask.sum().item()
    print(f'Test accuracy: {acc:.4f}')

# 使用PCA进行降维处理
pca = PCA(n_components=2)
data.x = pca.fit_transform(data.x)

# 绘制二维散点图
colors = [data.y[i] for i in range(len(data.y))]
plt.scatter(data.x[:, 0], data.x[:, 1], c=colors, cmap='viridis')
plt.colorbar()
plt.show()