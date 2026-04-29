const pool = require("../config/db");

async function checkSLA() {
  const now = new Date();

  // 🔹 1. Find overdue complaints
  const overdue = await pool.query(
    `SELECT * FROM complaints 
     WHERE status='pending' AND deadline < $1`,
    [now]
  );

  overdue.rows.forEach(c => {
    console.log(`🚨 ALERT: Complaint ${c.id} is overdue`);
  });

  // 🔹 2. Escalate after 7 days
  const escalate = await pool.query(
    `SELECT * FROM complaints 
     WHERE status='pending' 
     AND created_at < NOW() - INTERVAL '7 days'
     AND escalated = false`
  );

  for (let c of escalate.rows) {
    console.log(`⬆️ Escalating complaint ${c.id}`);

    await pool.query(
      `UPDATE complaints SET escalated = true WHERE id = $1`,
      [c.id]
    );
  }
}

module.exports = { checkSLA };