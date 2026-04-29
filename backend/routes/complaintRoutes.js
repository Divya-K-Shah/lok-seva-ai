const express = require("express");
const router = express.Router();

const {
  createComplaint,
  getComplaintById
} = require("../controllers/complaintController");

router.post("/complaints", createComplaint);
router.get("/complaints/:id", getComplaintById);

const { getAllComplaints, updateComplaint } = require("../controllers/complaintController");

router.get("/complaints", getAllComplaints);
router.put("/complaints/:id", updateComplaint);

module.exports = router;