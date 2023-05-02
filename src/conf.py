import yaml
from deepmerge import always_merger

with open('conf.yaml', 'r') as f:
    config = yaml.safe_load(f)

with open('conf_local.yaml', 'r') as f:
    local_config = yaml.safe_load(f)
    config.update(local_config)

if __name__ == "__main__":
    print(config)