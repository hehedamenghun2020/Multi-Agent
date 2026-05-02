# 🚀 Advanced Multi-Agent Task System

## 特点
- Multi-Agent Workflow
- Memory（可扩展 Redis）
- Tool Calling（模拟）# 🧠 Complex Task Decomposition Multi-Agent System

## 📌 项目简介

本项目是一个基于大模型构建的**复杂任务拆解与自动执行系统**。通过 **Multi-Agent 协作 + Workflow 编排机制**，系统可以将用户输入的高层目标自动拆解为多个子任务，并逐步完成信息检索、任务执行与结果校验，实现端到端自动化处理。

相比传统“问答式 AI”，本项目更关注**任务完成能力（Task Completion）**，适用于数据分析、运营执行、信息整理、技术辅助等复杂场景。

---

## 🎯 解决的核心问题

在实际业务中，复杂任务通常存在以下痛点：

* ❗ 需要人工进行多步拆解与规划
* ❗ 执行链路长（查询 → 处理 → 汇总）
* ❗ 强依赖上下文，步骤之间相互关联
* ❗ 自动化程度低，难以规模化执行

👉 本项目的目标是：
**让 AI 从“回答问题”升级为“自动完成复杂任务”**

---

## 🧠 系统架构（Multi-Agent）

系统采用模块化多 Agent 设计，每个 Agent 负责不同职责：

* **Planner Agent**：将复杂任务拆解为多个子任务
* **Research Agent**：检索信息、补充上下文
* **Execution Agent**：执行具体任务（支持工具调用）
* **QA Agent**：校验结果并生成最终输出
* **Memory 模块**：维护任务执行过程中的上下文状态

---

## 🔄 核心逻辑流（长链推理）

系统执行流程如下：

```
用户输入任务
   ↓
任务拆解（Planner）
   ↓
信息检索（Research）
   ↓
任务执行（Execution）
   ↓
结果校验（QA）
   ↓
输出最终结果
```

👉 形成完整闭环：
**任务理解 → 拆解 → 检索 → 执行 → 校验 → 汇总**

该流程具备典型的**长链推理能力**，能够处理多步骤、跨阶段的复杂任务。

---

## ⚙️ 技术栈

* Python
* 多 Agent 架构设计
* Workflow 编排（自定义 Engine）
* FastAPI（API 服务）
* 可扩展：Redis / 数据库 / 外部 API

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 启动 CLI

```bash
python main.py
```

### 3. 示例

```
输入复杂任务: 帮我分析一个电商用户增长策略
```

系统将自动：

* 拆解任务
* 执行子步骤
* 输出结构化结果

---

## 🌐 启动 API 服务

```bash
uvicorn app.api.server:app --reload
```

访问：

```
http://127.0.0.1:8000/run?task=你的任务
```

---

## 📊 项目特点

* ✅ 多 Agent 协作（职责清晰）
* ✅ 支持复杂任务拆解
* ✅ 长链推理能力（多步骤执行）
* ✅ Memory 上下文管理
* ✅ 可扩展 Tool Calling
* ✅ 支持 API 化部署

---

## 🧩 可扩展方向

* 接入真实 LLM（OpenAI / 本地模型）
* 引入 LangGraph / DAG 工作流
* 增加异步并发执行（async）
* 接入真实搜索/API工具
* 前端界面（Web UI）
* 任务持久化（Redis / DB）

---

## ⚠️ 注意事项

* 当前为示例项目，部分 Agent 为简化实现（mock）
* 生产环境建议：

  * 接入真实数据源
  * 增加日志 & 监控
  * 引入异常处理与重试机制

---

## 📌 总结

该项目展示了一个具备工程化能力的 Multi-Agent 系统，通过模块化设计与 Workflow 编排，实现复杂任务的自动拆解与执行，是从“对话型 AI”迈向“任务型 AI”的重要实践。

---

- 状态机执行流
- 可扩展为生产系统

## 启动
pip install -r requirements.txt
python main.py
