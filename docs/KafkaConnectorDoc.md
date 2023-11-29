## About the connector
Kubernetes, also known as K8s, is an open-source system for automating deployment, scaling, and management of containerized applications.
<p>This document provides information about the Kubernetes Connector, which facilitates automated interactions, with a Kubernetes server using FortiSOAR&trade; playbooks. Add the Kubernetes Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Kubernetes.</p>

### Version information

Connector Version: 1.0.0

Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-kubernetes</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Kubernetes server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Kubernetes server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Kubernetes</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the server URL on which K8s is hosted to connect and perform the automated operations.
</td>
</tr><tr><td>Token</td><td>Specify the token which you have generated for your service account. For more information refer <a>https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/</a>.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Apply YAML File</td><td>Deploys the manifest file in your K8s cluster.</td><td>apply_yml_file <br/>Investigation</td></tr>
<tr><td>Get Namespace Pods List</td><td>Retrieves all pods present in a namespace.</td><td>list_namespace_pod <br/>Investigation</td></tr>
<tr><td>Get Pod For All Namespaces</td><td>Retrieves all the pods from all namespaces.</td><td>list_pod_for_all_namespaces <br/>Investigation</td></tr>
<tr><td>Get Pod Logs</td><td>Retrieves the logs of a pod based on the namespace and pod name specified.</td><td>get_pod_logs <br/>Investigation</td></tr>
<tr><td>Delete Namespace Pods</td><td>Delete a pod present in a namespace.</td><td>delete_namespace_pod <br/>Investigation</td></tr>
<tr><td>Delete Collection Namespace Pods</td><td>Delete all pods present in a namespace.</td><td>delete_collection_namespace_pod <br/>Investigation</td></tr>
<tr><td>Delete Collection Namespace Secret</td><td>Delete all secrets present in a namespace.</td><td>delete_collection_namespace_secret <br/>Investigation</td></tr>
<tr><td>Delete Namespace Secret</td><td>Delete a secret present in a namespace.</td><td>delete_namespace_secret <br/>Investigation</td></tr>
<tr><td>List Secret For All Namespaces</td><td>Retrieves secrets present in all namespace.</td><td>list_secret_for_all_namespaces <br/>Investigation</td></tr>
<tr><td>Delete Collection Namespace ConfigMap</td><td>Delete all configmaps present in a namespace.</td><td>delete_collection_namespace_config_map <br/>Investigation</td></tr>
<tr><td>Delete Namespace ConfigMaps</td><td>Delete a configmap present in a namespace.</td><td>delete_namespace_config_map <br/>Investigation</td></tr>
<tr><td>Get ConfigMap For All Namespaces</td><td>Retrieves configmap present in all namespace.</td><td>list_config_map_for_all_namespaces <br/>Investigation</td></tr>
<tr><td>Get Events For All Namespaces</td><td>Retrieves events of all namespace.</td><td>list_event_for_all_namespaces <br/>Investigation</td></tr>
</tbody></table>

### operation: Apply YAML File
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Attachment IRI</td><td>IRI of the attachment that you want to submit.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "success": ""
}</pre>
### operation: Get Namespace Pods List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Namespace</td><td>Specify the namespace whose pods you want to retrieve.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "api_version": "",
    "items": [
        {
            "api_version": "",
            "kind": "",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": ""
                },
                "creation_timestamp": "",
                "deletion_grace_period_seconds": "",
                "deletion_timestamp": "",
                "finalizers": "",
                "generate_name": "",
                "generation": "",
                "labels": "",
                "managed_fields": [
                    {
                        "api_version": "",
                        "fields_type": "",
                        "fields_v1": {
                            "f:metadata": {
                                "f:annotations": {
                                    ".": {},
                                    "f:kubectl.kubernetes.io/last-applied-configuration": {}
                                }
                            },
                            "f:spec": {
                                "f:containers": {
                                    "k:{\"name\":\"c00\"}": {
                                        ".": {},
                                        "f:command": {},
                                        "f:image": {},
                                        "f:imagePullPolicy": {},
                                        "f:name": {},
                                        "f:resources": {},
                                        "f:terminationMessagePath": {},
                                        "f:terminationMessagePolicy": {}
                                    }
                                },
                                "f:dnsPolicy": {},
                                "f:enableServiceLinks": {},
                                "f:restartPolicy": {},
                                "f:schedulerName": {},
                                "f:securityContext": {},
                                "f:terminationGracePeriodSeconds": {}
                            }
                        },
                        "manager": "",
                        "operation": "",
                        "subresource": "",
                        "time": ""
                    }
                ],
                "name": "",
                "namespace": "",
                "owner_references": "",
                "resource_version": "",
                "self_link": "",
                "uid": ""
            },
            "spec": {
                "active_deadline_seconds": "",
                "affinity": "",
                "automount_service_account_token": "",
                "containers": [
                    {
                        "args": "",
                        "command": [],
                        "env": "",
                        "env_from": "",
                        "image": "",
                        "image_pull_policy": "",
                        "lifecycle": "",
                        "liveness_probe": "",
                        "name": "",
                        "ports": "",
                        "readiness_probe": "",
                        "resize_policy": "",
                        "resources": {
                            "claims": "",
                            "limits": "",
                            "requests": ""
                        },
                        "security_context": "",
                        "startup_probe": "",
                        "stdin": "",
                        "stdin_once": "",
                        "termination_message_path": "",
                        "termination_message_policy": "",
                        "tty": "",
                        "volume_devices": "",
                        "volume_mounts": [
                            {
                                "mount_path": "",
                                "mount_propagation": "",
                                "name": "",
                                "read_only": "",
                                "sub_path": "",
                                "sub_path_expr": ""
                            }
                        ],
                        "working_dir": ""
                    }
                ],
                "dns_config": "",
                "dns_policy": "",
                "enable_service_links": "",
                "ephemeral_containers": "",
                "host_aliases": "",
                "host_ipc": "",
                "host_network": "",
                "host_pid": "",
                "host_users": "",
                "hostname": "",
                "image_pull_secrets": "",
                "init_containers": "",
                "node_name": "",
                "node_selector": "",
                "os": "",
                "overhead": "",
                "preemption_policy": "",
                "priority": "",
                "priority_class_name": "",
                "readiness_gates": "",
                "resource_claims": "",
                "restart_policy": "",
                "runtime_class_name": "",
                "scheduler_name": "",
                "scheduling_gates": "",
                "security_context": {
                    "fs_group": "",
                    "fs_group_change_policy": "",
                    "run_as_group": "",
                    "run_as_non_root": "",
                    "run_as_user": "",
                    "se_linux_options": "",
                    "seccomp_profile": "",
                    "supplemental_groups": "",
                    "sysctls": "",
                    "windows_options": ""
                },
                "service_account": "",
                "service_account_name": "",
                "set_hostname_as_fqdn": "",
                "share_process_namespace": "",
                "subdomain": "",
                "termination_grace_period_seconds": "",
                "tolerations": [
                    {
                        "effect": "",
                        "key": "",
                        "operator": "",
                        "toleration_seconds": "",
                        "value": ""
                    }
                ],
                "topology_spread_constraints": "",
                "volumes": [
                    {
                        "aws_elastic_block_store": "",
                        "azure_disk": "",
                        "azure_file": "",
                        "cephfs": "",
                        "cinder": "",
                        "config_map": "",
                        "csi": "",
                        "downward_api": "",
                        "empty_dir": "",
                        "ephemeral": "",
                        "fc": "",
                        "flex_volume": "",
                        "flocker": "",
                        "gce_persistent_disk": "",
                        "git_repo": "",
                        "glusterfs": "",
                        "host_path": "",
                        "iscsi": "",
                        "name": "",
                        "nfs": "",
                        "persistent_volume_claim": "",
                        "photon_persistent_disk": "",
                        "portworx_volume": "",
                        "projected": {
                            "default_mode": "",
                            "sources": [
                                {
                                    "config_map": "",
                                    "downward_api": "",
                                    "secret": "",
                                    "service_account_token": {
                                        "audience": "",
                                        "expiration_seconds": "",
                                        "path": ""
                                    }
                                }
                            ]
                        },
                        "quobyte": "",
                        "rbd": "",
                        "scale_io": "",
                        "secret": "",
                        "storageos": "",
                        "vsphere_volume": ""
                    }
                ]
            },
            "status": {
                "conditions": [
                    {
                        "last_probe_time": "",
                        "last_transition_time": "",
                        "message": "",
                        "reason": "",
                        "status": "",
                        "type": ""
                    }
                ],
                "container_statuses": [
                    {
                        "allocated_resources": "",
                        "container_id": "",
                        "image": "",
                        "image_id": "",
                        "last_state": {
                            "running": "",
                            "terminated": "",
                            "waiting": ""
                        },
                        "name": "",
                        "ready": "",
                        "resources": "",
                        "restart_count": "",
                        "started": "",
                        "state": {
                            "running": {
                                "started_at": ""
                            },
                            "terminated": "",
                            "waiting": ""
                        }
                    }
                ],
                "ephemeral_container_statuses": "",
                "host_ip": "",
                "init_container_statuses": "",
                "message": "",
                "nominated_node_name": "",
                "phase": "",
                "pod_ip": "",
                "pod_i_ps": [
                    {
                        "ip": ""
                    }
                ],
                "qos_class": "",
                "reason": "",
                "resize": "",
                "start_time": ""
            }
        }
    ],
    "kind": "",
    "metadata": {
        "_continue": "",
        "remaining_item_count": "",
        "resource_version": "",
        "self_link": ""
    }
}</pre>
### operation: Get Pod For All Namespaces
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "api_version": "",
    "items": [
        {
            "api_version": "",
            "kind": "",
            "metadata": {
                "annotations": "",
                "creation_timestamp": "",
                "deletion_grace_period_seconds": "",
                "deletion_timestamp": "",
                "finalizers": "",
                "generate_name": "",
                "generation": "",
                "labels": {
                    "name": "",
                    "pod-template-hash": ""
                },
                "managed_fields": [
                    {
                        "api_version": "",
                        "fields_type": "",
                        "fields_v1": {
                            "f:metadata": {
                                "f:generateName": {},
                                "f:labels": {
                                    ".": {},
                                    "f:name": {},
                                    "f:pod-template-hash": {}
                                },
                                "f:ownerReferences": {
                                    ".": {},
                                    "k:{\"uid\":\"802584d1-ddf5-43d6-8d6a-1fb5800b7f34\"}": {}
                                }
                            },
                            "f:spec": {
                                "f:containers": {
                                    "k:{\"name\":\"c00\"}": {
                                        ".": {},
                                        "f:image": {},
                                        "f:imagePullPolicy": {},
                                        "f:name": {},
                                        "f:ports": {
                                            ".": {},
                                            "k:{\"containerPort\":80,\"protocol\":\"TCP\"}": {
                                                ".": {},
                                                "f:containerPort": {},
                                                "f:protocol": {}
                                            }
                                        },
                                        "f:resources": {
                                            ".": {},
                                            "f:limits": {
                                                ".": {},
                                                "f:cpu": {}
                                            },
                                            "f:requests": {
                                                ".": {},
                                                "f:cpu": {}
                                            }
                                        },
                                        "f:terminationMessagePath": {},
                                        "f:terminationMessagePolicy": {}
                                    }
                                },
                                "f:dnsPolicy": {},
                                "f:enableServiceLinks": {},
                                "f:restartPolicy": {},
                                "f:schedulerName": {},
                                "f:securityContext": {},
                                "f:terminationGracePeriodSeconds": {}
                            }
                        },
                        "manager": "",
                        "operation": "",
                        "subresource": "",
                        "time": ""
                    }
                ],
                "name": "",
                "namespace": "",
                "owner_references": [
                    {
                        "api_version": "",
                        "block_owner_deletion": "",
                        "controller": "",
                        "kind": "",
                        "name": "",
                        "uid": ""
                    }
                ],
                "resource_version": "",
                "self_link": "",
                "uid": ""
            },
            "spec": {
                "active_deadline_seconds": "",
                "affinity": "",
                "automount_service_account_token": "",
                "containers": [
                    {
                        "args": "",
                        "command": "",
                        "env": "",
                        "env_from": "",
                        "image": "",
                        "image_pull_policy": "",
                        "lifecycle": "",
                        "liveness_probe": "",
                        "name": "",
                        "ports": [
                            {
                                "container_port": "",
                                "host_ip": "",
                                "host_port": "",
                                "name": "",
                                "protocol": ""
                            }
                        ],
                        "readiness_probe": "",
                        "resize_policy": "",
                        "resources": {
                            "claims": "",
                            "limits": {
                                "cpu": ""
                            },
                            "requests": {
                                "cpu": ""
                            }
                        },
                        "security_context": "",
                        "startup_probe": "",
                        "stdin": "",
                        "stdin_once": "",
                        "termination_message_path": "",
                        "termination_message_policy": "",
                        "tty": "",
                        "volume_devices": "",
                        "volume_mounts": [
                            {
                                "mount_path": "",
                                "mount_propagation": "",
                                "name": "",
                                "read_only": "",
                                "sub_path": "",
                                "sub_path_expr": ""
                            }
                        ],
                        "working_dir": ""
                    }
                ],
                "dns_config": "",
                "dns_policy": "",
                "enable_service_links": "",
                "ephemeral_containers": "",
                "host_aliases": "",
                "host_ipc": "",
                "host_network": "",
                "host_pid": "",
                "host_users": "",
                "hostname": "",
                "image_pull_secrets": "",
                "init_containers": "",
                "node_name": "",
                "node_selector": "",
                "os": "",
                "overhead": "",
                "preemption_policy": "",
                "priority": "",
                "priority_class_name": "",
                "readiness_gates": "",
                "resource_claims": "",
                "restart_policy": "",
                "runtime_class_name": "",
                "scheduler_name": "",
                "scheduling_gates": "",
                "security_context": {
                    "fs_group": "",
                    "fs_group_change_policy": "",
                    "run_as_group": "",
                    "run_as_non_root": "",
                    "run_as_user": "",
                    "se_linux_options": "",
                    "seccomp_profile": "",
                    "supplemental_groups": "",
                    "sysctls": "",
                    "windows_options": ""
                },
                "service_account": "",
                "service_account_name": "",
                "set_hostname_as_fqdn": "",
                "share_process_namespace": "",
                "subdomain": "",
                "termination_grace_period_seconds": "",
                "tolerations": [
                    {
                        "effect": "",
                        "key": "",
                        "operator": "",
                        "toleration_seconds": "",
                        "value": ""
                    }
                ],
                "topology_spread_constraints": "",
                "volumes": [
                    {
                        "aws_elastic_block_store": "",
                        "azure_disk": "",
                        "azure_file": "",
                        "cephfs": "",
                        "cinder": "",
                        "config_map": "",
                        "csi": "",
                        "downward_api": "",
                        "empty_dir": "",
                        "ephemeral": "",
                        "fc": "",
                        "flex_volume": "",
                        "flocker": "",
                        "gce_persistent_disk": "",
                        "git_repo": "",
                        "glusterfs": "",
                        "host_path": "",
                        "iscsi": "",
                        "name": "",
                        "nfs": "",
                        "persistent_volume_claim": "",
                        "photon_persistent_disk": "",
                        "portworx_volume": "",
                        "projected": {
                            "default_mode": "",
                            "sources": [
                                {
                                    "config_map": "",
                                    "downward_api": "",
                                    "secret": "",
                                    "service_account_token": {
                                        "audience": "",
                                        "expiration_seconds": "",
                                        "path": ""
                                    }
                                }
                            ]
                        },
                        "quobyte": "",
                        "rbd": "",
                        "scale_io": "",
                        "secret": "",
                        "storageos": "",
                        "vsphere_volume": ""
                    }
                ]
            },
            "status": {
                "conditions": [
                    {
                        "last_probe_time": "",
                        "last_transition_time": "",
                        "message": "",
                        "reason": "",
                        "status": "",
                        "type": ""
                    }
                ],
                "container_statuses": [
                    {
                        "allocated_resources": "",
                        "container_id": "",
                        "image": "",
                        "image_id": "",
                        "last_state": {
                            "running": "",
                            "terminated": {
                                "container_id": "",
                                "exit_code": "",
                                "finished_at": "",
                                "message": "",
                                "reason": "",
                                "signal": "",
                                "started_at": ""
                            },
                            "waiting": ""
                        },
                        "name": "",
                        "ready": "",
                        "resources": "",
                        "restart_count": "",
                        "started": "",
                        "state": {
                            "running": {
                                "started_at": ""
                            },
                            "terminated": "",
                            "waiting": ""
                        }
                    }
                ],
                "ephemeral_container_statuses": "",
                "host_ip": "",
                "init_container_statuses": "",
                "message": "",
                "nominated_node_name": "",
                "phase": "",
                "pod_ip": "",
                "pod_i_ps": [
                    {
                        "ip": ""
                    }
                ],
                "qos_class": "",
                "reason": "",
                "resize": "",
                "start_time": ""
            }
        }
    ],
    "kind": "",
    "metadata": {
        "_continue": "",
        "remaining_item_count": "",
        "resource_version": "",
        "self_link": ""
    }
}</pre>
### operation: Get Pod Logs
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Pod Name</td><td>Specify the Pod name whose logs you want to retrieve.
</td></tr><tr><td>Namespace</td><td>Specify the namespace name where the pod exists.
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:

<pre>{
    "data": ""
}</pre>
### operation: Delete Namespace Pods
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Pod Name</td><td>Specify the Pod name which you want to delete.
</td></tr><tr><td>Namespace</td><td>Specify the namespace name where the pod exists.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "api_version": "",
    "kind": "",
    "metadata": {
        "annotations": {
            "kubectl.kubernetes.io/last-applied-configuration": ""
        },
        "creation_timestamp": "",
        "deletion_grace_period_seconds": "",
        "deletion_timestamp": "",
        "finalizers": "",
        "generate_name": "",
        "generation": "",
        "labels": "",
        "managed_fields": [
            {
                "api_version": "",
                "fields_type": "",
                "fields_v1": {
                    "f:metadata": {
                        "f:annotations": {
                            ".": {},
                            "f:kubectl.kubernetes.io/last-applied-configuration": {}
                        }
                    },
                    "f:spec": {
                        "f:containers": {
                            "k:{\"name\":\"c00\"}": {
                                ".": {},
                                "f:command": {},
                                "f:image": {},
                                "f:imagePullPolicy": {},
                                "f:name": {},
                                "f:resources": {},
                                "f:terminationMessagePath": {},
                                "f:terminationMessagePolicy": {}
                            }
                        },
                        "f:dnsPolicy": {},
                        "f:enableServiceLinks": {},
                        "f:restartPolicy": {},
                        "f:schedulerName": {},
                        "f:securityContext": {},
                        "f:terminationGracePeriodSeconds": {}
                    }
                },
                "manager": "",
                "operation": "",
                "subresource": "",
                "time": ""
            }
        ],
        "name": "",
        "namespace": "",
        "owner_references": "",
        "resource_version": "",
        "self_link": "",
        "uid": ""
    },
    "spec": {
        "active_deadline_seconds": "",
        "affinity": "",
        "automount_service_account_token": "",
        "containers": [
            {
                "args": "",
                "command": [],
                "env": "",
                "env_from": "",
                "image": "",
                "image_pull_policy": "",
                "lifecycle": "",
                "liveness_probe": "",
                "name": "",
                "ports": "",
                "readiness_probe": "",
                "resize_policy": "",
                "resources": {
                    "claims": "",
                    "limits": "",
                    "requests": ""
                },
                "security_context": "",
                "startup_probe": "",
                "stdin": "",
                "stdin_once": "",
                "termination_message_path": "",
                "termination_message_policy": "",
                "tty": "",
                "volume_devices": "",
                "volume_mounts": [
                    {
                        "mount_path": "",
                        "mount_propagation": "",
                        "name": "",
                        "read_only": "",
                        "sub_path": "",
                        "sub_path_expr": ""
                    }
                ],
                "working_dir": ""
            }
        ],
        "dns_config": "",
        "dns_policy": "",
        "enable_service_links": "",
        "ephemeral_containers": "",
        "host_aliases": "",
        "host_ipc": "",
        "host_network": "",
        "host_pid": "",
        "host_users": "",
        "hostname": "",
        "image_pull_secrets": "",
        "init_containers": "",
        "node_name": "",
        "node_selector": "",
        "os": "",
        "overhead": "",
        "preemption_policy": "",
        "priority": "",
        "priority_class_name": "",
        "readiness_gates": "",
        "resource_claims": "",
        "restart_policy": "",
        "runtime_class_name": "",
        "scheduler_name": "",
        "scheduling_gates": "",
        "security_context": {
            "fs_group": "",
            "fs_group_change_policy": "",
            "run_as_group": "",
            "run_as_non_root": "",
            "run_as_user": "",
            "se_linux_options": "",
            "seccomp_profile": "",
            "supplemental_groups": "",
            "sysctls": "",
            "windows_options": ""
        },
        "service_account": "",
        "service_account_name": "",
        "set_hostname_as_fqdn": "",
        "share_process_namespace": "",
        "subdomain": "",
        "termination_grace_period_seconds": "",
        "tolerations": [
            {
                "effect": "",
                "key": "",
                "operator": "",
                "toleration_seconds": "",
                "value": ""
            }
        ],
        "topology_spread_constraints": "",
        "volumes": [
            {
                "aws_elastic_block_store": "",
                "azure_disk": "",
                "azure_file": "",
                "cephfs": "",
                "cinder": "",
                "config_map": "",
                "csi": "",
                "downward_api": "",
                "empty_dir": "",
                "ephemeral": "",
                "fc": "",
                "flex_volume": "",
                "flocker": "",
                "gce_persistent_disk": "",
                "git_repo": "",
                "glusterfs": "",
                "host_path": "",
                "iscsi": "",
                "name": "",
                "nfs": "",
                "persistent_volume_claim": "",
                "photon_persistent_disk": "",
                "portworx_volume": "",
                "projected": {
                    "default_mode": "",
                    "sources": [
                        {
                            "config_map": "",
                            "downward_api": "",
                            "secret": "",
                            "service_account_token": {
                                "audience": "",
                                "expiration_seconds": "",
                                "path": ""
                            }
                        }
                    ]
                },
                "quobyte": "",
                "rbd": "",
                "scale_io": "",
                "secret": "",
                "storageos": "",
                "vsphere_volume": ""
            }
        ]
    },
    "status": {
        "conditions": [
            {
                "last_probe_time": "",
                "last_transition_time": "",
                "message": "",
                "reason": "",
                "status": "",
                "type": ""
            }
        ],
        "container_statuses": [
            {
                "allocated_resources": "",
                "container_id": "",
                "image": "",
                "image_id": "",
                "last_state": {
                    "running": "",
                    "terminated": "",
                    "waiting": ""
                },
                "name": "",
                "ready": "",
                "resources": "",
                "restart_count": "",
                "started": "",
                "state": {
                    "running": "",
                    "terminated": "",
                    "waiting": {
                        "message": "",
                        "reason": ""
                    }
                }
            }
        ],
        "ephemeral_container_statuses": "",
        "host_ip": "",
        "init_container_statuses": "",
        "message": "",
        "nominated_node_name": "",
        "phase": "",
        "pod_ip": "",
        "pod_i_ps": "",
        "qos_class": "",
        "reason": "",
        "resize": "",
        "start_time": ""
    }
}</pre>
### operation: Delete Collection Namespace Pods
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Namespace</td><td>Specify the namespace name from which you want to delete the pods.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "api_version": "",
    "code": "",
    "details": "",
    "kind": "",
    "message": "",
    "metadata": {
        "_continue": "",
        "remaining_item_count": "",
        "resource_version": "",
        "self_link": ""
    },
    "reason": "",
    "status": ""
}</pre>
### operation: Delete Collection Namespace Secret
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Namespace</td><td>Specify the namespace name from where to delete all secret.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "api_version": "",
    "code": "",
    "details": "",
    "kind": "",
    "message": "",
    "metadata": {
        "_continue": "",
        "remaining_item_count": "",
        "resource_version": "",
        "self_link": ""
    },
    "reason": "",
    "status": ""
}</pre>
### operation: Delete Namespace Secret
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Secret Name</td><td>Specify the Secret name which you want to delete.
</td></tr><tr><td>Namespace</td><td>Specify the namespace name from where to delete the secret.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "api_version": "",
    "code": "",
    "details": {
        "causes": "",
        "group": "",
        "kind": "",
        "name": "",
        "retry_after_seconds": "",
        "uid": ""
    },
    "kind": "",
    "message": "",
    "metadata": {
        "_continue": "",
        "remaining_item_count": "",
        "resource_version": "",
        "self_link": ""
    },
    "reason": "",
    "status": ""
}</pre>
### operation: List Secret For All Namespaces
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "api_version": "",
    "items": [
        {
            "api_version": "",
            "data": {
                "ca.crt": "",
                "namespace": "",
                "token": ""
            },
            "immutable": "",
            "kind": "",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "",
                    "kubernetes.io/service-account.name": "",
                    "kubernetes.io/service-account.uid": ""
                },
                "creation_timestamp": "",
                "deletion_grace_period_seconds": "",
                "deletion_timestamp": "",
                "finalizers": "",
                "generate_name": "",
                "generation": "",
                "labels": "",
                "managed_fields": [
                    {
                        "api_version": "",
                        "fields_type": "",
                        "fields_v1": {
                            "f:data": {
                                ".": {},
                                "f:ca.crt": {},
                                "f:namespace": {},
                                "f:token": {}
                            },
                            "f:metadata": {
                                "f:annotations": {
                                    "f:kubernetes.io/service-account.uid": {}
                                }
                            }
                        },
                        "manager": "",
                        "operation": "",
                        "subresource": "",
                        "time": ""
                    }
                ],
                "name": "",
                "namespace": "",
                "owner_references": "",
                "resource_version": "",
                "self_link": "",
                "uid": ""
            },
            "string_data": "",
            "type": ""
        }
    ],
    "kind": "",
    "metadata": {
        "_continue": "",
        "remaining_item_count": "",
        "resource_version": "",
        "self_link": ""
    }
}</pre>
### operation: Delete Collection Namespace ConfigMap
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Namespace</td><td>Specify the namespace name from where you want to delete all the configmaps.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "api_version": "",
    "code": "",
    "details": "",
    "kind": "",
    "message": "",
    "metadata": {
        "_continue": "",
        "remaining_item_count": "",
        "resource_version": "",
        "self_link": ""
    },
    "reason": "",
    "status": ""
}</pre>
### operation: Delete Namespace ConfigMaps
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>ConfigMap Name</td><td>Specify the ConfigMap name which you want to delete.
</td></tr><tr><td>Namespace</td><td>Specify the namespace name from where you want to delete the configmaps.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "api_version": "",
    "code": "",
    "details": {
        "causes": "",
        "group": "",
        "kind": "",
        "name": "",
        "retry_after_seconds": "",
        "uid": ""
    },
    "kind": "",
    "message": "",
    "metadata": {
        "_continue": "",
        "remaining_item_count": "",
        "resource_version": "",
        "self_link": ""
    },
    "reason": "",
    "status": ""
}</pre>
### operation: Get ConfigMap For All Namespaces
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "api_version": "",
    "items": [
        {
            "api_version": "",
            "binary_data": "",
            "data": {
                "ca.crt": ""
            },
            "immutable": "",
            "kind": "",
            "metadata": {
                "annotations": {
                    "kubernetes.io/description": ""
                },
                "creation_timestamp": "",
                "deletion_grace_period_seconds": "",
                "deletion_timestamp": "",
                "finalizers": "",
                "generate_name": "",
                "generation": "",
                "labels": "",
                "managed_fields": [
                    {
                        "api_version": "",
                        "fields_type": "",
                        "fields_v1": {
                            "f:data": {
                                ".": {},
                                "f:ca.crt": {}
                            },
                            "f:metadata": {
                                "f:annotations": {
                                    ".": {},
                                    "f:kubernetes.io/description": {}
                                }
                            }
                        },
                        "manager": "",
                        "operation": "",
                        "subresource": "",
                        "time": ""
                    }
                ],
                "name": "",
                "namespace": "",
                "owner_references": "",
                "resource_version": "",
                "self_link": "",
                "uid": ""
            }
        }
    ],
    "kind": "",
    "metadata": {
        "_continue": "",
        "remaining_item_count": "",
        "resource_version": "",
        "self_link": ""
    }
}</pre>
### operation: Get Events For All Namespaces
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "api_version": "",
    "items": [
        {
            "action": "",
            "api_version": "",
            "count": "",
            "event_time": "",
            "first_timestamp": "",
            "involved_object": {
                "api_version": "",
                "field_path": "",
                "kind": "",
                "name": "",
                "namespace": "",
                "resource_version": "",
                "uid": ""
            },
            "kind": "",
            "last_timestamp": "",
            "message": "",
            "metadata": {
                "annotations": "",
                "creation_timestamp": "",
                "deletion_grace_period_seconds": "",
                "deletion_timestamp": "",
                "finalizers": "",
                "generate_name": "",
                "generation": "",
                "labels": "",
                "managed_fields": [
                    {
                        "api_version": "",
                        "fields_type": "",
                        "fields_v1": {
                            "f:count": {},
                            "f:firstTimestamp": {},
                            "f:involvedObject": {},
                            "f:lastTimestamp": {},
                            "f:message": {},
                            "f:reason": {},
                            "f:source": {
                                "f:component": {},
                                "f:host": {}
                            },
                            "f:type": {}
                        },
                        "manager": "",
                        "operation": "",
                        "subresource": "",
                        "time": ""
                    }
                ],
                "name": "",
                "namespace": "",
                "owner_references": "",
                "resource_version": "",
                "self_link": "",
                "uid": ""
            },
            "reason": "",
            "related": "",
            "reporting_component": "",
            "reporting_instance": "",
            "series": "",
            "source": {
                "component": "",
                "host": ""
            },
            "type": ""
        }
    ],
    "kind": "",
    "metadata": {
        "_continue": "",
        "remaining_item_count": "",
        "resource_version": "",
        "self_link": ""
    }
}</pre>
## Included playbooks
The `Sample - kubernetes - 1.0.0` playbook collection comes bundled with the Kubernetes connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Kubernetes connector.

- Apply YAML File
- Delete Collection Namespace ConfigMap
- Delete Collection Namespace Pods
- Delete Collection Namespace Secret
- Delete Namespace ConfigMaps
- Delete Namespace Pods
- Delete Namespace Secret
- Get ConfigMap For All Namespaces
- Get Events For All Namespaces
- Get Namespace Pods List
- Get Pod For All Namespaces
- Get Pod Logs
- List Secret For All Namespaces

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
