import db from "../../lib/connect-db";

export async function GET(request: Request) {
  const _db = await db();

  if (!_db) {
    return new Response(
      JSON.stringify({
        error: "Database not connected",
      }),
      {
        headers: {
          "content-type": "application/json",
        },
        status: 500,
      }
    );
  }

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
