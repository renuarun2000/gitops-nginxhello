import yaml
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--customer', action='store', type=str, required=True)

args =  my_parser.parse_args()

customerNS = "template/{0}/namespace.yaml".format(args.customer)
customerPod = "template/{0}/pod.yaml".format(args.customer)

destCustomerNSFile = "Customers/{0}/namespace.yaml".format(args.customer)
destCustomerPodFile = "template/{0}/pod.yaml".format(args.customer)

with open(customerNS, "r") as stream:
    try:
        nsYaml = yaml.safe_load(stream)
        nsYaml["metadata"]["name"] = args.customer
    except Exception as exc:
        print(exc)

with open(destCustomerNSFile, "w") as nsFile:
    try:
        yaml.dump(nsYaml, nsFile)
    except Exception as exc:
        print(exc)

with open(customerPod, "r") as stream:
    try:
        podYaml = yaml.safe_load(stream)
        nsYaml["metadata"]["namespace"] = args.customer
    except Exception as exc:
        print(exc)

with open(destCustomerPodFile, "w") as podFile:
    try:
        yaml.dump(podYaml, podFile)
    except Exception as exc:
        print(exc)

