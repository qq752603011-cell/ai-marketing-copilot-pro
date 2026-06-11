# 🚀 AI Marketing Copilot V3

企业级 AI 营销内容生成平台

基于 Python + Streamlit + DeepSeek API 开发，输入产品信息后一键生成全套营销内容，自动同步飞书多维表格，支持 AI 小红书封面图生成。

---

## ✨ 项目功能

### 营销内容一键生成
输入产品名称、特点、目标客户，自动生成：
- 商品标题（3条，含关键词）
- 封面标题（5条，强冲击力）
- 核心卖点（5条）
- 小红书图文文案（800字，含 emoji）
- 短视频口播稿（适合 30-60 秒）
- 亚马逊 Bullet Point（英文，5条）

### AI 小红书封面图生成
- 5 种场景模板：产品平铺 / 生活场景 / 简约纯色 / 户外场景 / 礼盒展示
- 支持自定义提示词
- 基于硅基流动图像生成 API（Kolors / SDXL）

### 自动同步飞书多维表格
- 各字段分列写入（商品标题、文案、卖点等独立保存）
- 产品图片和 AI 封面图自动上传为附件

### 批量模式
- 上传 CSV 文件，批量生成多个产品的营销内容
- 一键导出 Excel（每行一个产品，各字段分列）

### 多格式导出
- Word (.docx)
- Excel (.xlsx)

---

## 🛠 技术栈

| 模块 | 技术 |
|------|------|
| 前端 | Streamlit |
| 后端 | Python 3 |
| 文案生成 | DeepSeek API（deepseek-chat / deepseek-reasoner）|
| 图像生成 | 硅基流动 API（Kwai-Kolors/Kolors、SDXL）|
| 数据库 | 飞书多维表格（Bitable API）|
| 文件处理 | python-docx、openpyxl |
| 版本管理 | Git + GitHub |

---

## 📸 项目截图

（可添加项目运行截图）

---

## 🚀 本地运行

**安装依赖：**

```bash
pip install -r requirements.txt
```

**启动项目：**

```bash
streamlit run app.py
```

---

## 🔑 环境变量

创建 `.streamlit/secrets.toml`：

```toml
DEEPSEEK_API_KEY = "your_deepseek_api_key"
SILICONFLOW_API_KEY = "your_siliconflow_api_key"
FEISHU_APP_ID = "your_feishu_app_id"
FEISHU_APP_SECRET = "your_feishu_app_secret"
BASE_ID = "your_bitable_base_id"
TABLE_ID = "your_bitable_table_id"
```

> ⚠️ 请确保 `.streamlit/secrets.toml` 已加入 `.gitignore`，不要上传到 GitHub。

---

## 🗂 飞书表格字段配置

飞书多维表格需包含以下字段：

| 字段名 | 类型 |
|--------|------|
| 商品标题 | 文本 |
| 封面标题 | 文本 |
| 核心卖点 | 文本 |
| 小红书文案 | 文本 |
| 短视频口播稿 | 文本 |
| 亚马逊卖点 | 文本 |
| 产品图片 | 附件 |
| 小红书封面 | 附件 |

---

## 👩‍💻 作者

**阿晓AI**

独立开发 AI 应用，专注跨境电商 + AI 工具方向。