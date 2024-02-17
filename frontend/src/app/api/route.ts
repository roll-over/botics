import db from "./../../lib/connect-db";

export async function GET(request: Request) {
  const _db = await db();

  const collection = _db.collection("users");

  const result = await collection
    .find(
      {},
      {
        projection: {
          _id: 0,
          username: 1,
        },
      }
    )
    .toArray();

  try {
    return new Response(JSON.stringify(result), {
      headers: {
        "content-type": "application/json",
      },
    });
  } catch (e) {
    console.error(e);
    return new Response(
      JSON.stringify({
        error: e,
      }),
      {
        headers: {
          "content-type": "application/json",
        },
        status: 500,
      }
    );
  }
}
