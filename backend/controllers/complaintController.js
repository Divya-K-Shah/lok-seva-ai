const axios = require("axios");
const pool = require("../config/db");

// 🔹 Category → Department Mapping
const departmentMap = {
  road: "Road & Traffic management Department",
  garbage: "Solid Waste Management",
  streetlight: "Electric Department",
  water: "Water Supply Department",
  sewage: "Sewage & Drainage Department",
  encroachment: "Encroachment Department"
};

// 🔹 Priority Keywords
const urgentWords = ["urgent", "immediately", "asap", "जल्दी", "तुरंत"];

// 🔹 Priority Function
function getPriority(text) {
  const lowerText = text.toLowerCase();
  return urgentWords.some(word => lowerText.includes(word))
    ? "high"
    : "medium";
}

exports.getAllComplaints = async (req,res)=>{

  try{

    const result = await pool.query(
      "SELECT * FROM complaints ORDER BY created_at DESC"
    )

    res.json(result.rows)

  }catch(err){
    console.error(err)
    res.status(500).json({error:"server error"})
  }

}


exports.updateComplaint = async (req,res)=>{

  const {id} = req.params
  const {status} = req.body

  try{

    await pool.query(
      "UPDATE complaints SET status=$1 WHERE id=$2",
      [status,id]
    )

    res.json({message:"updated"})

  }catch(err){
    console.error(err)
    res.status(500).json({error:"server error"})
  }

}

// 🔹 Main Controller
exports.createComplaint = async (req, res) => {
  const complaint = req.body.complaint || req.body.complaint_text;

  // ✅ Safety check
  if (!complaint) {
    return res.status(400).json({ error: "Complaint is required" });
  }

  try {
    // 🔹 Call Python ML API
    const mlResponse = await axios.post("http://localhost:5000/predict", {
      complaint: complaint,
    });

    let category = (mlResponse.data.category || "").toLowerCase();

    // 🔹 Normalize properly (VERY IMPORTANT FIX)
    if (category.includes("road")) {
      category = "road";
    } else if (category.includes("traffic")) {
      category = "road";
    } else if (category.includes("garbage") || category.includes("waste")) {
      category = "garbage";
    } else if (category.includes("water")) {
      category = "water";
    } else if (category.includes("sewage")) {
      category = "sewage";
    }

// const lowerText = complaint.toLowerCase();

// // 🔹 Sewage keywords
// const sewageKeywords = ["drain", "sewage", "nala", "नाला", "नाली"];
// // 🔹 Traffic keywords
// const trafficKeywords = ["traffic", "signal", "ट्रैफिक"];

// // 🔹 Override logic
// if (sewageKeywords.some(word => lowerText.includes(word))) {
//   category = "sewage";
// }


    // 🔹 Department routing
    const department = departmentMap[category] || "General";

    // 🔹 Priority detection
    const priority = getPriority(complaint);

    // 🔹 Insert into DB
    const now = new Date();
let deadline = new Date();

// 🔹 SLA logic
if (priority === "high") {
  deadline.setDate(now.getDate() + 2);
} else {
  deadline.setDate(now.getDate() + 4);
}

const result = await pool.query(
  `INSERT INTO complaints 
  (complaint_text, category, priority, status, department, deadline, created_at)
  VALUES ($1, $2, $3, $4, $5, $6, $7)
  RETURNING *`,
  [complaint, category, priority, "pending", department, deadline, now]
);

    // 🔹 Response
    res.status(201).json({
      message: "Complaint registered",
      data: result.rows[0],
    });

  } catch (error) {
    console.error("ERROR:", error.message);
    res.status(500).json({ error: "Something went wrong" });
  }
};

//Get complaint by ID

exports.getComplaintById = async (req, res) => {

  const { id } = req.params;

  try {

    const result = await pool.query(
      "SELECT * FROM complaints WHERE id=$1",
      [id]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({ error: "Complaint not found" });
    }

    res.json(result.rows[0]);

  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Server error" });
  }

};