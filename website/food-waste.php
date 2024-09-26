<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Food Waste Reduction Dashboard</title>
    <link rel="stylesheet" href="foodstyle.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>

    <!-- Sidebar -->
    <div class="sidebar">
        <div class="logo">
            <img src="food logo.png" alt="Food Rescue Logo">
        </div>
        <ul>
            <li><a href="food-waste.php" class="active"><i class="fas fa-tachometer-alt"></i> Dashboard</a></li>
            <li><a href="donor.html"><i class="fas fa-donate"></i> Donor</a></li>
            <li><a href="#"><i class="fas fa-user"></i> User</a></li>
            <li><a href="volunteer.html"><i class="fas fa-hands-helping"></i> Volunteer</a></li>
            <li><a href="#"><i class="fas fa-utensils"></i> Listed Foods</a></li>
            <li><a href="#"><i class="fas fa-recycle"></i> Waste Management</a></li>
            <li><a href="#"><i class="fas fa-trash-alt"></i> Waste Food</a></li>
            <li><a href="#"><i class="fas fa-file-alt"></i> Report</a></li>
        </ul>
    </div>

    <!-- Main Content -->
    <div class="main-content">
        <header>
            <h2>Dashboard</h2>
        </header>

        <div class="statistics">
            <div class="stat-item">
                <h3>0</h3>
                <p>Total Food List</p>
            </div>
            <div class="stat-item">
                <h3>0</h3>
                <p>Total Donors</p>
            </div>
            <div class="stat-item">
                <h3>0</h3>
                <p>Total Users</p>
            </div>
            <div class="stat-item">
                <h3>0</h3>
                <p>Total Food Waste</p>
            </div>
        </div>

        <!-- Pie Chart Section -->
        <div class="chart-section">
            <h3>Activity Status</h3>
            <div class="pie-chart-placeholder">
                <!-- Pie Chart Placeholder -->
                <p>Pie Chart</p>
            </div>
        </div>

        <!-- Total Foods Table -->
        <div class="table-section">
            <h3>Total Foods</h3>
            <table>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Food Name</th>
                        <th>Food Quantity</th>
                        <th>Food Description</th>
                        <th>Food Type</th>
                        <th>Food Expiry Date</th>
                        <th>Image</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>Biryani</td>
                        <td>23</td>
                        <td>Very Good Biryani</td>
                        <td><span class="tag non-veg">Non-Veg</span></td>
                        <td>2023-07-26</td>
                        <td><img src="biryani.jpg" alt="Biryani Image"></td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td>Bhendi</td>
                        <td>23</td>
                        <td>Good Bhendi</td>
                        <td><span class="tag veg">Veg</span></td>
                        <td>2023-02-15</td>
                        <td><img src="bhendi.jpg" alt="Bhendi Image"></td>
                    </tr>
                    <tr>
                        <td>3</td>
                        <td>Dhokla</td>
                        <td>22</td>
                        <td>Good Taste</td>
                        <td><span class="tag veg">Veg</span></td>
                        <td>2023-08-31</td>
                        <td><img src="dhokla.jpg" alt="Dhokla Image"></td>
                    </tr>
                </tbody>
            </table>
        </div>

    </div>

</body>
</html>
