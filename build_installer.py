#!/usr/bin/env python3
import os

def build_installer():
    skill_path = "SKILL.md"
    installer_path = "install.sh"
    
    if not os.path.exists(skill_path):
        print(f"Error: {skill_path} not found.")
        return
        
    with open(skill_path, "r") as f:
        skill_content = f.read()
        
    install_template = f'''#!/usr/bin/env bash

# vaib (Vibe-Accelerated Intent Blocks) Global Installer
# Generated dynamically via GitHub Actions compiler

set -e

SKILL_DIR="\\$HOME/.claude/skills/vaib"
REF_DIR="\\$SKILL_DIR/references"

echo "🌊 Initializing vaib framework installation..."

mkdir -p "\\$SKILL_DIR"
mkdir -p "\\$REF_DIR"

# Write the core logic engine exactly as compiled
cat << 'EOF' > "\\$SKILL_DIR/SKILL.md"
{skill_content}
EOF

# Write a baseline web reference file if it does not exist
if [ ! -f "\\$REF_DIR/web-core.md" ]; then
cat << 'EOF' > "\\$REF_DIR/web-core.md"
# vaib Core Web Reference Dictionary
## Data & Migration Shortcodes
- `db_connect!`: Setup transactional pooled connection with health check pings.
- `schema_sync!`: Handle relational schema safety, applying safe table migrations or throwing errors on data truncation risks.
## API & Controller Shortcodes
- `endpoint: GET /path`: Generate standard HTTP controller routing with automatic serialization.
- `resource: CRUD`: Scaffolding macro. Generates standard database lifecycle pipelines (Create, Read, Update, Delete) for the current State block.
EOF
fi

echo "✨ vaib installation complete!"
echo "🚀 Run 'claude' and type '/skills' to verify integration."
'''

    with open(installer_path, "w") as f:
        f.write(install_template)
        
    os.chmod(installer_path, 0o755)
    print("🚀 install.sh compiled successfully from SKILL.md and permissions updated!")

if __name__ == "__main__":
    build_installer()
