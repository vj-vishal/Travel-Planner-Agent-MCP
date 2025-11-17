# 🌍 Travel Planner Agent
An **AI-powered travel assistant** that automates routing, cab booking, hotel reservations, and itinerary generation using **MCP**, **Ola Maps**, and **Claude Sonnet**.

<img width="1527" height="906" alt="Image" src="https://github.com/user-attachments/assets/d2a198db-9021-4a7f-9dc1-4cf3bbecc9bd" />

## 🎯 Overview

Travel Planner Agent is an intelligent assistant that takes the hassle out of trip planning by:
- Finding optimal routes between multiple destinations
- Booking transportation (cabs) automatically
- Reserving hotel accommodations
- Creating detailed, time-optimized itineraries
- Providing comprehensive travel recommendations

Perfect for travelers who want a seamless, all-in-one planning experience!

## ✨ Features

### 🗺️ **Intelligent Route Planning**
- Geocoding for location discovery
- Multi-stop route optimization
- Real-time distance and duration calculations
- Traffic-aware routing using Ola Maps API

### 🚕 **Transportation Booking**
- Automated cab booking service integration
- Pickup and dropoff scheduling
- Driver assignment and tracking
- Booking confirmation with reference IDs

### 🏨 **Accommodation Management**
- Hotel availability checking
- Automatic booking and confirmation
- Location-based hotel recommendations

### 📅 **Smart Itinerary Generation**
- Time-optimized schedules
- Activity recommendations
- Buffer time for meals and rest
- Detailed attraction information

### 💡 **Travel Intelligence**
- Must-visit location suggestions
- Local cuisine recommendations
- Budget estimates
- Weather and timing considerations

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│         Travel Planner Agent (AI)           │
│              (Claude Sonnet)                │
└──────────────┬──────────────────────────────┘
               │
      ┌────────┴────────┐
      │                 │
      ▼                 ▼
┌──────────┐    ┌──────────────┐
│ Ola Maps │    │   Booking    │
│   MCP    │    │   Services   │
│ Server   │    │     MCP      │
└────┬─────┘    └──────┬───────┘
     │                 │
     ├─────────────────┼──────────────────┐
     │                 │                  │
     ▼                 ▼                  ▼
┌─────────┐    ┌──────────┐    ┌──────────────┐
│ Geocode │    │   Cab    │    │    Hotel     │
│   API   │    │ Booking  │    │   Booking    │
└─────────┘    │   API    │    │     API      │
┌─────────┐    └──────────┘    └──────────────┘
│ Routing │
│   API   │
└─────────┘
┌─────────┐
│  Route  │
│Optimizer│
└─────────┘
```

### Technology Stack
- **AI Model**: Claude Sonnet 4.5 (Anthropic)
- **Protocol**: Model Context Protocol (MCP)
- **Maps API**: Ola Maps Platform
- **Booking Services**: Custom MCP-enabled booking APIs
- **Language**: Python 3.8+

## 📦 Prerequisites

Before you begin, ensure you have:

- Python 3.8 or higher
- Claude API access (Anthropic)
- Ola Maps API key
- MCP server setup
- Booking service credentials (if using real services)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/vj-vishal/travel-planner-agent.git
cd travel-planner-agent
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Anthropic** - For Claude AI and MCP protocol
- **Ola Maps** - For comprehensive mapping and routing APIs
- **Open Source Community** - For various tools and libraries used in this project



