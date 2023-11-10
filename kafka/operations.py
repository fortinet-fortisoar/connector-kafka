"""
Copyright start
MIT License
Copyright (c) 2023 Fortinet Inc
Copyright end
"""

from connectors.core.connector import get_logger, ConnectorError
import requests, json, time
from kafka import KafkaProducer, KafkaConsumer


logger = get_logger('kafka')

def topic_list(config, params, *args, **kwargs):

    server = "{}:{}".format(config.get('host'), config.get('port'))
    consumer = KafkaConsumer(bootstrap_servers=server)

    try:
        result = consumer.topics()
        return result.json()
    except Exception as err:
        logger.exception("Error getting topic list from Kafka. Error as follows: {}".format(str(err)))
        raise ConnectorError("Error getting topic list from Kafka. Error as follows: {}".format(str(err)))

def topic_details(config, params, *args, **kwargs):

    server = "{}:{}".format(config.get('host'), config.get('port'))
    consumer = KafkaConsumer(params.get('topics'), bootstrap_servers=server)


    try:
        consumer.subscription()
        consumer.topics()
        consumer.seek_to_beginning()
        p = consumer.poll(timeout_ms=1000)
        return p.json()
    except Exception as err:
        logger.exception("Error getting topic list from Kafka. Error as follows: {}".format(str(err)))
        raise ConnectorError("Error getting topic list from Kafka. Error as follows: {}".format(str(err)))

def post_topic(config, params, *args, **kwargs):

    server = "{}:{}".format(config.get('host'), config.get('port'))
    producer = KafkaProducer(bootstrap_servers=server)
    topic_name = params.get('topic')
    topic_message = json.dumps(params.get('message')).encode('utf-8')

    try:
        m = producer.send(topic_name, topic_message)

        i = 0
        while not m.is_done:
            logger.info("checking done attempt {0}".format(str(i)))
            logger.info(m.is_done)
            i += 1
            time.sleep(2)

        if m.is_done:
            pass
            return m.get().json()

    except Exception as err:
        logger.exception("Error posting data to Kafka. Error as follows: {}".format(str(err)))
        raise ConnectorError("Error posting data to Kafka. Error as follows: {}".format(str(err)))


def _check_health(config):

    headers = {'Accept': 'application/vnd.kafka.v2+json'}
    url = 'http://{}:{}'.format(config.get('host'), config.get('port'))

    try:
        result = requests.get(url, headers=headers)
        if result.status_code == 200:
            return True
        else:
            return result.json()
            logger.exception("Error connecting to Kafka. Error as follows: {}".format(result.json()))
            raise ConnectorError("Error connecting to Kafka. Error as follows: {}".format(result.json()))
    except Exception as err:
        logger.exception("Error connecting to Kafka. Error as follows: {}".format(str(err)))
        raise ConnectorError("Error connecting to Kafka. Error as follows: {}".format(str(err)))


operations = {
    'topic_list': topic_list,
    'topic_details': topic_details,
    'post_topic': post_topic
}

