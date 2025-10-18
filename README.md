🚀 ##Features
🔐 ##Authentication System
User Registration - Create new accounts with secure validation

User Login - Secure authentication system

Profile Management - Update personal information and passwords

Session Management - Secure user sessions

📝 ##Task Management
Create Tasks - Add new tasks with details like title, description, priority, and estimated time

View Tasks - Beautiful card-based task display with progress tracking

Update Tasks - Edit existing task information

Delete Tasks - Mark tasks as complete with confirmation

Search Functionality - Find tasks quickly with search feature

Priority System - Color-coded priority levels (High, Medium, Low)

Progress Tracking - Visual progress bars for task completion

🎨 ##Modern UI/UX
Glassmorphism Design - Beautiful translucent glass-like elements

Responsive Layout - Works perfectly on all device sizes

Smooth Animations - Elegant transitions and hover effects

Modern Color Scheme - Professional gradient backgrounds

Interactive Elements - Hover effects and micro-interactions

🛠️ ##Technology Stack
Backend: Django 4.2

Frontend: HTML5, CSS3, JavaScript

Styling: Custom CSS with Glassmorphism effects

Database: SQLite (default) 

Fonts: System fonts with fallbacks

🎯 ##Pages Overview
🏠 ##Home Page (home.html)
Hero section with call-to-action buttons

Modern gradient background with glassmorphism effects

Responsive design for all screen sizes

🔐 ##Authentication Pages
Sign In (signin.html): Clean login form with validation

Sign Up (signup.html): User registration with multiple fields

Profile (profile.html): User dashboard with avatar and stats

Update Profile (updateProfile.html): Edit user information

Update Password (updatePass.html): Secure password change

📋 ##Task Management Pages
Create Task (create.html): Form to add new tasks

Display Tasks (display.html): Grid layout of all tasks with search

Specific Task (specific.html): Detailed task view with actions

Update Task (update.html): Edit existing task details

Delete Task (deleteTask.html): Confirmation dialog for task completion

🚀 ##Installation & Setup

Clone the repository
bash
git clone https://github.com/s01dier-0f-g0d/task_manager.git
cd task_manager

Create virtual environment
bash
python -m venv venv
source venv/bin/activate  
On Windows: venv\Scripts\activate

Run migrations
bash
python manage.py migrate

Create superuser
bash
python manage.py createsuperuser

Run development server
bash
python manage.py runserver

Access the application
http://localhost:8000
