const express = require("express");
const app = express();
const cron = require("node-cron");
const { checkSLA } = require("./services/slaService");  

// ✅ ADD THIS LINE
app.use(express.json());

const complaintRoutes = require("./routes/complaintRoutes");

app.use("/", complaintRoutes);

app.listen(3000, () => {
  console.log("Server running on port 3000");

  // 🔹 Run SLA check every 1 minute
  cron.schedule("*/1 * * * *", () => {
    console.log("⏱️ Running SLA check...");
    checkSLA();
  });
});