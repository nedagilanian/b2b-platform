import React, { useEffect, useState } from "react";
import api from "../services/api";

function Orders() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
     api.get("/orders/orders") // گرفتن لیست سفارشات از بک‌اند
      .then(response => {
        setOrders(response.data);
      })
      .catch(error => console.error("خطا در دریافت سفارشات:", error));
  }, []);

  return (
    <div>
      <h1>لیست سفارشات</h1>
      <ul>
        {orders.map(order => (
          <li key={order.id}>
            سفارش شماره {order.id} - وضعیت: {order.status}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Orders;
