import kubernetes.client as k8s_client
import kubernetes.config as k8s_config

exchange_rate_crd = k8s_client.V1CustomResourceDefinition(
    api_version="apiextensions.k8s.io/v1",
    kind="CustomResourceDefinition",
    metadata=k8s_client.V1ObjectMeta(
        name="copyrators.operators.datapm.pomm"),
    spec=k8s_client.V1CustomResourceDefinitionSpec(
        group="operators.datapm.pommo",
        versions=[k8s_client.V1CustomResourceDefinitionVersion(
            name="v1",
            served=True,
            storage=True,
            schema=k8s_client.V1CustomResourceValidation(
                open_apiv3_schema=k8s_client.V1JSONSchemaProps(
                    type="object",
                    properties={"ruleType": k8s_client.V1JSONSchemaProps(
                        type="string"
                    ),
                        "namespace": k8s_client.V1JSONSchemaProps(
                        type="string"
                    ),
                        "selector": k8s_client.V1JSONSchemaProps(
                        type="object",
                        properties={"copyrator": k8s_client.V1JSONSchemaProps(
                            type="string"
                        )},
                    ),
                    },
                )
            )
        )],
        scope="Namespaced",
        names=k8s_client.V1CustomResourceDefinitionNames(
            plural="copyrators",
            singular="copyrator",
            kind="CopyratorRule",
            short_names=["copyr"]
        )
    )
)

k8s_config.load_kube_config()

with k8s_client.ApiClient() as api_client:
    api_instance = k8s_client.ApiextensionsV1Api(api_client)
    try:
        api_instance.create_custom_resource_definition(exchange_rate_crd)
    except k8s_client.rest.ApiException as e:
        if e.status == 409:  # if the CRD already exists the K8s API will respond with a 409 Conflict
            print("CRD already exists")
        else:
            raise e
