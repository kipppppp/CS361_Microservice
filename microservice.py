import asyncio
import websockets
import json
import pymongo


async def data(websocket):
    """
    Sends JSON data to the client
    :param websocket
    """
    client = db_connect()
    final_score = process_data(client)

    send_data = {"Final Score": final_score}

    return_data = json.dumps(send_data)
    await websocket.send(return_data)


async def main():
    """
    Listens for incoming connections at
    HOST: 127.0.0.1
    PORT: 65432
    """
    async with websockets.serve(data, "127.0.0.1", 65432):
        await asyncio.Future()


def db_connect() -> pymongo:
    """
    Connect to mongodb from python using pymongo
    :return: pymongo client object
    """
    # Insert credentials here XXXX
    return pymongo.MongoClient("XXXX")


def process_data(client: pymongo) -> int:
    """
    Process data from mongodb to find total team score
    :param client: pymongo client object
    :return: int
    """
    # Open the DB
    dbname = client['test']

    # Get players collection
    players = dbname["players"]

    # Parse collection
    entries_list = []
    for entry in players.find():
        entry_list = [entry['passingYards'], entry['receptions'], entry['receivingYards'], entry['rushingYards'], entry['fumbles'], entry['interceptions']]
        entries_list.append(entry_list)

    summation = [0, 0, 0, 0, 0, 0]

    # Calculate the sum for each statistic
    for player in entries_list:
        for stat in range(0,len(player)):
            summation[stat] = summation[stat] + player[stat]

    scoring_values = dbname["stats"]

    # Obtain value for each statistic and add to the stat_list
    stat_list = None
    for statistic in scoring_values.find():
        stat_list = [statistic['passingYards'], statistic['receptions'], statistic['receivingYards'], statistic['rushingYards'], statistic['fumbles'], statistic['interceptions']]

    # Calculate point value for each statistic
    total_score = []
    for i in range(0, len(stat_list)):
        total_score.append((stat_list[i] * summation[i]))

    print(sum(total_score))
    return sum(total_score)


if __name__ == "__main__":
    asyncio.run(main())
