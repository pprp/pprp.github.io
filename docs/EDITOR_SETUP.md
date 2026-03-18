# 博客在线编辑器设置指南

## 功能特性

- ✅ 在线 Markdown 编辑器
- ✅ 实时预览
- ✅ 一键发布到 GitHub
- ✅ 权限控制（仅授权用户可访问）
- ✅ 支持中英双语标题

## 快速设置（3步）

### 1. 启用 GitHub OAuth

在 GitHub 仓库设置中：
- Settings → Security → Deploy keys
- 或使用 Netlify Identity（推荐）

### 2. 部署到 Netlify（推荐）

```bash
# 如果还没有部署到 Netlify
# 1. 访问 https://app.netlify.com
# 2. 连接你的 GitHub 仓库
# 3. 构建命令: bundle exec jekyll build
# 4. 发布目录: _site
```

### 3. 启用 Netlify Identity

在 Netlify 控制台：
1. Site settings → Identity → Enable Identity
2. Registration → Invite only（仅邀请）
3. Services → Git Gateway → Enable
4. 邀请你自己的邮箱

## 使用方法

访问：`https://你的域名/admin/`

首次访问：
1. 点击"Sign up"
2. 检查邮箱确认邀请
3. 设置密码
4. 登录后即可编辑博客

## 权限控制

**方式1：Netlify Identity（推荐）**
- 只有被邀请的邮箱才能注册
- 在 Netlify 控制台管理用户
- 完全免费

**方式2：GitHub OAuth**
- 只有仓库协作者可以访问
- 在 GitHub 仓库设置中管理权限

## 本地测试

如果使用 GitHub 作为后端，需要配置：

```yaml
# admin/config.yml
backend:
  name: github
  repo: pprp/pprp.github.io
  branch: main
```

然后访问 `http://localhost:4000/admin/`

## 故障排查

**问题：无法登录**
- 检查 Netlify Identity 是否启用
- 确认邮箱已被邀请

**问题：无法保存**
- 检查 Git Gateway 是否启用
- 确认 GitHub 权限正确

## 文件说明

- `admin/config.yml` - CMS 配置
- `admin/index.html` - 编辑器页面
- 编辑器会自动创建/更新 `_posts/` 下的文件
