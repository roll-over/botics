import { MongoClient } from "mongodb";

const ME_CONFIG_MONGODB_URL = process.env.ME_CONFIG_MONGODB_URL;

if (!ME_CONFIG_MONGODB_URL) {
  throw new Error("ME_CONFIG_MONGODB_URL is not set");
}

const client = new MongoClient(ME_CONFIG_MONGODB_URL);

let db = null;

export const startMongo = async () => {
  console.log("Starting mongo");
  for (let i = 0; i < 10; i++) {
    try {
      await client.connect();
      db = client.db("collaboration");
      break;
    } catch (e) {
      console.error(e);
      await new Promise((resolve) => setTimeout(resolve, 1000));
    }
  }
  return client;
};

export default async () => {
  if (db) {
    return db;
  } else {
    await startMongo();
    return db;
  }
};
