-- Question 1. How many active subscriptions were present as of 3/1/2020?
SELECT COUNT(DISTINCT Subscription_ID) AS ActiveSubscriptions
FROM Subscriptions_Snapshot_Dataset
WHERE EFFECTIVE_START_DATE <= '2020-03-01'
  AND EFFECTIVE_END_DATE >= '2020-03-01';

-- Question 2. What were the expected renewal dates associated with the active subscriptions in (1)?
WITH ActiveSubscriptions AS (
  SELECT DISTINCT Subscription_ID
  FROM Subscriptions_Snapshot_Dataset
  WHERE EFFECTIVE_START_DATE <= '2020-03-01'
    AND EFFECTIVE_END_DATE >= '2020-03-01'
)SELECT
  a.Subscription_ID,
  MAX(b.EFFECTIVE_END_DATE) AS ExpectedRenewalDate
FROM
  ActiveSubscriptions a
JOIN
  Subscriptions_Snapshot_Dataset b ON a.Subscription_ID = b.Subscription_ID
WHERE
  b.EFFECTIVE_END_DATE >= '2020-03-01'
GROUP BY
  a.Subscription_ID;

-- Question 3. How many of the subscriptions identified in (1) renewed?

WITH ActiveSubscriptions AS (
  SELECT DISTINCT Subscription_ID
  FROM Subscriptions_Snapshot_Dataset
  WHERE EFFECTIVE_START_DATE <= '2020-03-01'
    AND EFFECTIVE_END_DATE >= '2020-03-01'
)SELECT
  COUNT(DISTINCT a.Subscription_ID) AS RenewedSubscriptions
FROM
  ActiveSubscriptions a
JOIN
  Subscriptions_Snapshot_Dataset b ON a.Subscription_ID = b.Subscription_ID
WHERE
  b.EFFECTIVE_START_DATE <= '2020-03-01' + INTERVAL 30 DAY
  AND b.EFFECTIVE_END_DATE >= '2020-03-01';

-- Question 4. What potential issues do you see with identifying renewals using your method in (3) vs. actually identifying the renewal subscription version with a unique key?

-- Answer : 1. One potential issue is that the 30-day interval might not be sufficient for all cases, and some renewals might be missed. Also, if the renewal process involves more complex logic, this simplistic approach may not capture all renewals accurately.
--          2. Date format in mentioned so it is bit ambiguous for ex. YYYY/MM/DD or MM/DD/YYYY or DD/MM/YY etc .
--          3. Accuracy of Renewal Identification:

--          If Snapshot_ID is solely based on the creation date of the snapshot and not on the actual subscription events, it may not accurately represent the renewal events.
--          Renewals could occur between two snapshot dates, and relying on snapshot creation dates might not capture these intermediate events.
--          Ambiguity in Snapshot Creation Frequency:

--          If snapshots are not taken at regular intervals, the date proximity approach might not be consistent. Some renewals could be missed if they fall between two snapshots.
--          Handling Late Renewals or Early Terminations:

--          If a subscription renews late or terminates early, its start date might not align closely with the end date of the previous version, leading to misclassifications.
--          Dependency on Snapshot Frequency:

--          The method heavily depends on the frequency of snapshot creation. Higher snapshot frequency reduces the chances of missing renewals but increases the storage and processing overhead.