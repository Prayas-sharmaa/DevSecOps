#!/usr/bin/env python3
import json
import subprocess
import sys


EB_ENV_NAME = "store-management-env"   # <<< change if needed


def get_instance_ids():
    try:
        result = subprocess.check_output([
            "aws", "elasticbeanstalk", "describe-environment-resources",
            "--environment-name", EB_ENV_NAME,
            "--query", "EnvironmentResources.Instances[*].Id",
            "--output", "json"
        ])
        return json.loads(result)
    except Exception as e:
        print(json.dumps({}))
        sys.exit(1)


def main():
    if "--list" in sys.argv:
        instance_ids = get_instance_ids()

        inventory = {
            "_meta": {
                "hostvars": {}
            },
            "eb": {
                "hosts": instance_ids
            }
        }

        print(json.dumps(inventory, indent=2))
    elif "--host" in sys.argv:
        print(json.dumps({}))
    else:
        print(json.dumps({}))


if __name__ == "__main__":
    main()
