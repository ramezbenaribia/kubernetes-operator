import kubernetes.client as k8s_client
import kubernetes.config as k8s_config

from .const import CRD_GROUP, CRD_PLURAL, CRD_VERSION


__all__ = [
    'load_crd',
]


def load_crd(CRD_OBJECT_NAMESPACE, CRD_RULE_NAME):

    api_client = k8s_client.ApiClient()
    api_instance = k8s_client.CustomObjectsApi(api_client)
    try:
        crd = api_instance.get_namespaced_custom_object(
            CRD_GROUP,
            CRD_VERSION,
            CRD_OBJECT_NAMESPACE,
            CRD_PLURAL,
            CRD_RULE_NAME
        )
        return {x: crd[x] for x in ('ruleType',  'selector', 'namespace')}

    except k8s_client.rest.ApiException as e:
        if e.status == 404:  # if the CRD dosen't exists the K8s API will respond with a 404 Conflict
            print("CRD dosen't exists")
            return
        else:
            raise e
