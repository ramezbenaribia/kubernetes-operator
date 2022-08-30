import kubernetes.client as k8s_client
import kubernetes.config as k8s_config
from fastapi import FastAPI


def viewNameSP():
    try:
        k8s_config.load_incluster_config()
    except:
        k8s_config.load_kube_config()
    arr = []

    v1 = k8s_client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        arr.append({
            "pod_ip": i.status.pod_ip,
            "namespace": i.metadata.namespace,
            "name": i.metadata.name
        })
    return arr


app = FastAPI()


@app.get("/")
def read_root():
    return viewNameSP()
