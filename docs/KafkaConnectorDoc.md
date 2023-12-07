
<h2>About the connector</h2>

<p>Kafka is an open-source distributed event streaming platform. This Kafka Connector is use to publish/consume a messages to/from a topic.</p>

<p>This document provides information about the Kafka Connector, which facilitates automated interactions, with a Kafka server using FortiSOAR&trade; playbooks. Add the Kafka Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Kafka.</p>

<h3>Version information</h3>

<p>Connector Version: 1.0.0</p>

<p>Authored By: Fortinet</p>

<p>Certified: No</p>

<h2>Installing the connector</h2>

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>

<pre>yum install cyops-connector-kafka</pre>

<h2>Prerequisites to configuring the connector</h2>

<ul>
<li>You must have the credentials of Kafka server to which you will connect and perform automated operations.</li>
<li>The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Kafka server.</li>
</ul>

<h2>Minimum Permissions Required</h2>

<ul>
<li>Not applicable</li>
</ul>

<h2>Configuring the connector</h2>

<p>For the procedure to configure a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector">here</a></p>

<h3>Configuration parameters</h3>

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Kafka</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Hostname</td><td>Specify the hostname to connect.</td>
</tr><tr><td>Port</td><td>Specify the port number to connect.</td>
</tr></tbody></table>

<h2>Actions supported by the connector</h2>

<p>The following automated operations can be included in playbooks and you can also use the annotations to access operations:</p>

<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>kafka topic list</td><td>Retrieves all topics that are on the Kafka.</td><td> <br/></td></tr>
<tr><td>kafka topic details</td><td>Get details of topic(s) based on the topic names and other input parameters specified from Kafka</td><td> <br/></td></tr>
<tr><td>Send String Message to Topic</td><td>Publish Message to a Topic in Kafka</td><td> <br/></td></tr>
<tr><td>Send b64encoded Message to Topic</td><td>Publish Message to a Topic in Kafka The b64encoded message will be decoded to bytes</td><td> <br/></td></tr>
</tbody></table>

<h3>operation: kafka topic list</h3>

<h4>Input parameters</h4>

<p>None.</p>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h3>operation: kafka topic details</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Topic Names</td><td>Specify the topic names whose details you want to fetch.
</td></tr><tr><td>Poll Timeout in ms</td><td>Specify the Poll Timeout in ms
</td></tr><tr><td>Max Records</td><td>Specify the maximum records to fetch.
</td></tr><tr><td>Seek Partition</td><td>sample input value: 
[
    {
        "partition": 1,
        "offset": 1,
    }
]
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h3>operation: Send String Message to Topic</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Topic</td><td>Specify the topic to which you want to send the message
</td></tr><tr><td>Message</td><td>Specify the message to send.
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h3>operation: Send b64encoded Message to Topic</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Topic</td><td>Specify the topic to which you want to send the message
</td></tr><tr><td>Base64 Message</td><td>Specify the message to send.
</td></tr></tbody></table>

<h4>Output</h4>

<p>No output schema is available at this time.</p>

<h2>Included playbooks</h2>

<p>The <code>Sample - kafka - 1.0.0</code> playbook collection comes bundled with the Kafka connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the <strong>Automation</strong> &gt; <strong>Playbooks</strong> section in FortiSOAR&trade; after importing the Kafka connector.</p>

<ul>
<li>Send String Message to Topic</li>
<li>Send b64encoded Message to Topic</li>
<li>kafka topic details</li>
<li>kafka topic list</li>
</ul>

<p><strong>Note</strong>: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.</p>
