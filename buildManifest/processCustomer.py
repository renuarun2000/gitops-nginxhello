import yaml
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--customer', action='store', type=str, required=True)

args =  my_parser.parse_args()

customerNS = "template/namespace.yaml"
customerPod = "template/pod.yaml"

destCustomerNSFile = "Customers/{0}/namespace.yaml".format(args.customer)
destCustomerPodFile = "Customers/{0}/pod.yaml".format(args.customer)

with open(customerNS, "r") as stream:
    try:
        nsYaml = yaml.load(stream)
        nsYaml["metadata"]["name"] = args.customer
    except Exception as exc:
        print(exc)

with open(destCustomerNSFile, "w") as nsFile:
    try:
        yaml.dump(nsYaml, nsFile, default_flow_style=False)
    except Exception as exc:
        print(exc)

with open(customerPod, "r") as stream:
    try:
        podYaml = yaml.safe_load(stream)
        podYaml["metadata"]["namespace"] = args.customer
    except Exception as exc:
        print(exc)

with open(destCustomerPodFile, "w") as podFile:
    try:
        yaml.dump(podYaml, podFile, default_flow_style=False)
    except Exception as exc:
        print(exc)

print(nsYaml)
print(podYaml)

