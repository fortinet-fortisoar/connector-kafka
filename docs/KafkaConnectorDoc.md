## About the connector
Kafka is an open-source distributed event streaming platform. This Kafka Connector is use to publish/consume a messages to/from a topic.
<p>This document provides information about the Kafka Connector, which facilitates automated interactions, with a Kafka server using FortiSOAR&trade; playbooks. Add the Kafka Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Kafka.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-kafka</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Kafka server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Kafka server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Kafka</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Hostname</td><td>Specify the hostname to connect.
</td>
</tr><tr><td>Port</td><td>Specify the port number to connect.
</td>
</tr></tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Kafka Topic List</td><td>Retrieves all topics that are on the Kafka.</td><td>topic_list <br/>Investigation</td></tr>
<tr><td>Kafka Topic Details</td><td>Get details of topic(s) based on the topic names and other input parameters specified from Kafka</td><td>topic_details <br/>Investigation</td></tr>
<tr><td>Send String Message to Topic</td><td>Publish Message to a Topic in Kafka</td><td>send_str_message_to_topic <br/>Investigation</td></tr>
<tr><td>Send b64encoded Message to Topic</td><td>Publish Message to a Topic in Kafka The b64encoded message will be decoded to bytes</td><td>send_b64encoded_message_to_topic <br/>Investigation</td></tr>
</tbody></table>

### operation: Kafka Topic List
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Kafka Topic Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Topic Names</td><td>Specify the topic names whose details you want to fetch.
</td></tr><tr><td>Poll Timeout in ms</td><td>Specify the Poll Timeout in ms
</td></tr><tr><td>Max Records</td><td>Specify the maximum records to fetch.
</td></tr><tr><td>Seek Partition</td><td>Specify the seek partition.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Send String Message to Topic
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Topic</td><td>Specify the topic to which you want to send the message
</td></tr><tr><td>Message</td><td>Specify the message to send.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Send b64encoded Message to Topic
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Topic</td><td>Specify the topic to which you want to send the message
</td></tr><tr><td>Base64 Message</td><td>Specify the message to send.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - kafka - 1.0.0` playbook collection comes bundled with the Kafka connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Kafka connector.

- Send String Message to Topic
- Send b64encoded Message to Topic
- Kafka Topic Details
- Kafka Topic List

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
