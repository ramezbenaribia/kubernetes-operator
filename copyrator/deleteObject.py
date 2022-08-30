from cmath import pi
import kubernetes.client as k8s_client
import kubernetes.config as k8s_config


def delete_crd():
    k8s_config.load_kube_config()

    with k8s_client.ApiClient() as api_client:
        api_instance = k8s_client.CustomObjectsApi(api_client)
        try:
            crd = api_instance.delete_namespaced_custom_object(
                'operators.brennerm.github.io',
                'v1',
                'default',
                'exchangerates',
                'exchange-rate-usd',
            )
            print(crd)

        except k8s_client.rest.ApiException as e:
            if e.status == 404:  # if the CRD dosen't exists the K8s API will respond with a 404 Conflict
                print("CRD dosen't exists")
                return
            else:
                raise e
