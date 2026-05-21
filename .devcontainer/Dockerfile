FROM mcr.microsoft.com/devcontainers/python:1-3.13-bookworm
# Remove stale Yarn apt repository whose GPG key is no longer valid.
# This would otherwise cause apt-get update to fail when devcontainer features run.
RUN rm -f /etc/apt/sources.list.d/yarn.list /usr/share/keyrings/yarnkey.gpg

# Install Node.js LTS via fnm (required for npx-based MCP servers)
RUN curl -fsSL https://fnm.vercel.app/install | bash -s -- --install-dir /usr/local/fnm --skip-shell \
    && /usr/local/fnm/fnm install --lts \
    && ln -sf /usr/local/fnm/aliases/lts-latest/bin/node /usr/local/bin/node \
    && ln -sf /usr/local/fnm/aliases/lts-latest/bin/npm /usr/local/bin/npm \
    && ln -sf /usr/local/fnm/aliases/lts-latest/bin/npx /usr/local/bin/npx
