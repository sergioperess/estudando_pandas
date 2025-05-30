
-- CTRL + SHIFT + Q

SELECT seller_id,
       sum(t1.price) AS totalRevenue,
       count(DISTINCT t1.order_id) AS qtSalles

FROM tb_order_items as t1

GROUP BY seller_id

