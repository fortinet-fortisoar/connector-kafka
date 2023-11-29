"""
Copyright start
MIT License
Copyright (c) 2023 Fortinet Inc
Copyright end
"""

# %%
from connectors.core.connector import get_logger, ConnectorError
import json
from base64 import b64decode, b64encode
from kafka import KafkaProducer, KafkaConsumer, TopicPartition
from kafka.producer.future import RecordMetadata
from kafka.consumer.fetcher import ConsumerRecord


logger = get_logger("kafka")

DEFAULT_ENCODING_CODEC = "utf-8"


class DannyJSONEncoder(json.JSONEncoder):
    global DEFAULT_ENCODING_CODEC

    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode(DEFAULT_ENCODING_CODEC)
        elif isinstance(obj, TopicPartition):
            return obj._asdict()
        elif isinstance(obj, RecordMetadata):
            return obj._asdict()
        return json.JSONEncoder.default(self, obj)


def convert_item_to_value(item):
    if isinstance(item, list):
        return convert_list_to_jsonDict(item)

    elif isinstance(item, dict):
        return convert_dict_to_jsonDict(item)

    elif isinstance(item, bytes):
        return item.decode(DEFAULT_ENCODING_CODEC)

    elif isinstance(item, TopicPartition):
        return convert_dict_to_jsonDict(item._asdict())

    elif isinstance(item, ConsumerRecord):
        return convert_dict_to_jsonDict(item._asdict())

    elif isinstance(item, RecordMetadata):
        return convert_dict_to_jsonDict(item._asdict())

    else:
        return item


def convert_list_to_jsonDict(_list: list) -> list:
    retval = []
    for _item in _list:
        if isinstance(_item, list):
            retval.append(convert_list_to_jsonDict(_item))

        elif isinstance(_item, dict):
            retval.append(convert_dict_to_jsonDict(_item))

        else:
            retval.append(convert_item_to_value(_item))

    return retval


def convert_dict_to_jsonDict(_dict: dict) -> dict:
    for _key in _dict:
        if isinstance(_dict[_key], list):
            _dict[_key] = convert_list_to_jsonDict(_dict[_key])

        elif isinstance(_dict[_key], dict):
            _dict[_key] = convert_dict_to_jsonDict(_dict[_key])

        else:
            _dict[_key] = convert_item_to_value(_dict[_key])

    return _dict


def topic_list(config: dict, params: dict):
    host = config.get("host")
    port = config.get("port", "9092")

    consumer = KafkaConsumer(bootstrap_servers=f"{host}:{port}")

    try:
        result = consumer.topics()
        return list(result)
    except Exception as err:
        raise ConnectorError(f"{err}")


def topic_details(config: dict, params: dict):
    host = config.get("host")
    port = config.get("port", "9092")

    topics = params.get("topics")
    poll_timeout_ms = params.get("poll_timeout_ms", 1000)
    max_records = params.get("max_records", None)
    seek_partition = params.get("seek_partition", list)

    global DEFAULT_ENCODING_CODEC
    DEFAULT_ENCODING_CODEC = params.get("msg_decode_codec", "utf-8")
    # must be in the format [{"partition": "partition_name", "offset": 0}]

    try:
        consumer = KafkaConsumer(bootstrap_servers=f"{host}:{port}")
        consumer.subscribe(topics)
        consumer.topics()

        kafka_topic_result_list = []
        if isinstance(seek_partition, list) and len(seek_partition) > 0:
            assign_partition = []
            for _seek_po in seek_partition:
                partition = _seek_po.get("partition")
                offset = _seek_po.get("offset", 0)

                for _assignment in consumer.assignment():
                    if _assignment.partition == partition:
                        assign_partition.append(
                            {"partition": _assignment, "offset": offset}
                        )

            for _partition in assign_partition:
                consumer.seek(_partition.get("partition"), _partition.get("offset"))
                kafka_topic_result_list.append(
                    consumer.poll(poll_timeout_ms, max_records)
                )
        else:
            consumer.seek_to_beginning()
            kafka_topic_result_list.append(consumer.poll(poll_timeout_ms, max_records))

        return convert_item_to_value(kafka_topic_result_list)
    except Exception as err:
        raise ConnectorError(f"{err}")


def send_str_message_to_topic(config: dict, params: dict):
    host = config.get("host")
    port = config.get("port", "9092")

    producer = KafkaProducer(bootstrap_servers=f"{host}:{port}")

    topic = params.get("topic", "")
    msg = params.get("message", "")
    msg_encode_codec = params.get("msg_encode_codec", "utf-8")

    try:
        msg = producer.send(topic, msg.encode(msg_encode_codec))
        return convert_item_to_value(msg.get())

    except Exception as err:
        raise ConnectorError(f"{err}")


def send_b64encoded_message_to_topic(config: dict, params: dict):
    host = config.get("host")
    port = config.get("port", "9092")

    producer = KafkaProducer(bootstrap_servers=f"{host}:{port}")

    topic = params.get("topic", "")
    base64_msg = params.get("base64msg", "")

    try:
        msg = producer.send(topic, b64decode(base64_msg))
        return convert_item_to_value(msg.get())

    except Exception as err:
        raise ConnectorError(f"{err}")


def _check_health(config: dict):
    return topic_list(config, None)


operations = {
    "topic_list": topic_list,
    "topic_details": topic_details,
    "send_str_message_to_topic": send_str_message_to_topic,
    "send_b64encoded_message_to_topic": send_b64encoded_message_to_topic,
}

# For debugging purpose
# %%
# usage test!
# config = {
#     "host": "127.0.0.1",
#     "port": "9092",
# }
# asd = _check_health(config)
# topic_list(config, None)

# params = {
#     "topic": "topic1",
#     "msg": "hello",
#     "msg_encode_codec": "utf-8",
#     "base64_msg": b64encode("hello".encode("utf-8")).decode("utf-8"),
# }
# send_str_message_to_topic(config, params)
# send_b64encoded_message_to_topic(config, params)

# params = {
#     "topics": ["topic1", "my-topic"],
#     "seek_partition": [
#         {
#             "partition": 1,
#             "offset": 1,
#         }
#     ],
# }
# asd = topic_details(config, params)