---check points: not in 
---solution 1 Runtime: 191 ms
select request_at day,
      ROUND(sum(case when status = 'completed' then 0 else 1 end)/count(*),2) "Cancellation Rate"
 from trips t
where 
      request_at between '2013-10-01' and '2013-10-03'
  and t.client_id in (select users_id from users where banned = 'No' and role = 'client')
  and t.driver_id in (select users_id from users where banned = 'No' and role = 'driver')
group by request_at

---solution 1 Runtime: 212 ms
select request_at day,
      CAST(sum(case when status = 'completed' then 0 else 1 end)/count(*) AS DECIMAL(18,2)) "Cancellation Rate"
 from trips t
where 
      request_at between '2013-10-01' and '2013-10-03'
  and t.client_id in (select users_id from users where banned = 'No' and role = 'client')
  and t.driver_id in (select users_id from users where banned = 'No' and role = 'driver')
group by request_at
