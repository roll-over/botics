"use client";

import { useState, useEffect } from "react";

export default function AllUsers() {
  const [users, setUsers] = useState([] as any[]);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/")
      .then((res) => res.json())
      .then((data) => {
        setUsers(data);
        setLoading(false);
      });
  }, []);

  if (isLoading) {
    return <p>Loading...</p>;
  }
  if (!users) {
    return <p>No profile data</p>;
  }

  return (
    <div className="p-10">
      <h1 className="text-2xl">All Users</h1>
      <ul className="pl-5 list list-disc">
        {users.map((user) => (
          <li key={user.username}>{user.username}</li>
        ))}
      </ul>
    </div>
  );
}
