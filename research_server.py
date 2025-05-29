import json
from typing import List, Dict, Any
from mcp.server.fastmcp import FastMCP # Assuming mcp.server.fastmcp is available

# Initialize FastMCP server for the Google Ads mock
mcp = FastMCP("google_ads_mock")

def generate_ford_mach_e_creatives(campaign_id: str) -> List[Dict[str, Any]]:
    """
    Generates a highly verbose and detailed list of mock ad creatives
    for a Ford Mustang Mach-E campaign.
    """
    
    # --- Creative 1: Focused on Performance and Thrill ---
    performance_creative = {
        "ad_creative_id": f"creative_{campaign_id}_performance",
        "campaign_id": campaign_id,
        "theme": "Performance, Speed, and Exhilaration",
        "status": "ENABLED",
        "type": "RESPONSIVE_SEARCH_AD",
        "assets": {
            "headlines": [
                "Experience the Thrill of the Mustang Mach-E",
                "Ford Mustang Mach-E | 0-60 MPH in 3.8s",
                "Electrifying Performance is Here",
                "Book Your Exhilarating Test Drive Today",
                "Unbridled Power, Zero Emissions",
                "How Fast is the Mach-E GT?",
                "Feel the Instant Electric Torque",
                "Reserve Your Electric Pony Now",
                "Performance That Gives You Goosebumps",
                "The Legend, Reimagined for Electric"
            ],
            "descriptions": [
                "The Ford Mustang Mach-E GT Performance Edition delivers breathtaking speed, going from 0 to 60 mph in just 3.8 seconds. Feel the immediate, heart-pounding power of its all-electric drivetrain and experience a ride that's both exhilarating and uniquely Mustang. It's the new shape of freedom.",
                "With up to 480 horsepower and 634 lb.-ft. of torque, the Mustang Mach-E GT offers truly scintillating performance. The available eAWD provides precise handling and traction, letting you confidently carve corners and master any road condition. Choose your experience with selectable drive modes, including Whisper, Engage, and the thrilling Unbridled mode for ultimate performance.",
                "Ready to feel the future of performance? The Mustang Mach-E is waiting for you. Schedule a test drive at your local dealer and discover how Ford has redefined the thrill of driving. All electric, all soul, all Mustang. Your adventure awaits."
            ],
            "image_assets": [
                {
                    "asset_id": "img_101_perf",
                    "name": "mach_e_gt_in_motion_cyber_orange.jpg",
                    "alt_text": "A Ford Mustang Mach-E GT in Cyber Orange speeding on a winding road.",
                    "description": "This dynamic shot captures the essence of the Mach-E's performance, showcasing its athletic stance and a sense of motion. It is ideal for ad copy focusing on speed, handling, and the exhilaration of the drive."
                }
            ],
            "sitelink_extensions": [
                {"text": "Build & Price Your GT", "final_url": "https://www.ford.com/suvs/mach-e/build-and-price/gt/"},
                {"text": "View Performance Specs", "final_url": "https://www.ford.com/suvs/mach-e/features/performance/"},
                {"text": "Compare Drive Modes", "final_url": "https://www.ford.com/suvs/mach-e/features/drive-modes/"}
            ]
        }
    }

    # --- Creative 2: Focused on Technology and Connectivity ---
    technology_creative = {
        "ad_creative_id": f"creative_{campaign_id}_technology",
        "campaign_id": campaign_id,
        "theme": "Advanced Technology, Connectivity, and Safety",
        "status": "ENABLED",
        "type": "RESPONSIVE_SEARCH_AD",
        "assets": {
            "headlines": [
                "The Intelligent Mustang Mach-E",
                "SYNC 4A: Your Personal Assistant",
                "Ford Co-Pilot360™ Technology",
                "Drive Hands-Free with BlueCruise",
                "A Smarter, More Connected Drive",
                "What is Ford Co-Pilot360?",
                "Seamless Smartphone Integration",
                "Future-Forward Tech Inside",
                "Your Cockpit, Reimagined"
            ],
            "descriptions": [
                "Interact with your Mustang Mach-E through the stunning 15.5-inch touchscreen powered by SYNC 4A. This adaptive system learns your preferences, making personalized suggestions and providing cloud-connected navigation, conversational voice commands, and seamless smartphone integration with Apple CarPlay and Android Auto.",
                "Experience the future of driving with Ford BlueCruise, the available hands-free highway driving technology. It allows you to take your hands off the wheel on prequalified sections of divided highways called Hands-Free Blue Zones. The system is monitored by a driver-facing camera to ensure you're keeping your eyes on the road.",
                "Drive with more confidence thanks to the standard Ford Co-Pilot360™ Technology. This suite of driver-assist features includes Pre-Collision Assist with Automatic Emergency Braking, a Rear View Camera, BLIS® (Blind Spot Information System) with Cross-Traffic Alert, and a Lane-Keeping System."
            ],
             "video_assets": [
                {
                    "asset_id": "vid_201_tech",
                    "name": "mach_e_sync_4a_demonstration.mp4",
                    "youtube_id": "mock_youtube_id_tech_demo",
                    "description": "A detailed walkthrough of the 15.5-inch SYNC 4A touchscreen, showing its machine learning capabilities, customizable interface, and seamless integration with navigation and apps."
                }
            ],
            "sitelink_extensions": [
                {"text": "Explore SYNC 4A", "final_url": "https://www.ford.com/technology/sync/sync-4a/"},
                {"text": "Learn About BlueCruise", "final_url": "https://www.ford.com/technology/bluecruise/"},
                {"text": "Ford Co-Pilot360 Details", "final_url": "https://www.ford.com/technology/co-pilot360/"}
            ]
        }
    }
    
    # --- Creative 3: Focused on Range, Charging, and Practicality ---
    practicality_creative = {
        "ad_creative_id": f"creative_{campaign_id}_practicality",
        "campaign_id": campaign_id,
        "theme": "EV Range, Charging Solutions, and Everyday Practicality",
        "status": "PAUSED", # Paused for variety
        "type": "RESPONSIVE_SEARCH_AD",
        "assets": {
            "headlines": [
                "Go the Distance in a Mach-E",
                "EPA-Est. Range of 312 Miles",
                "Charge Easily at Home or on the Go",
                "BlueOval™ Charge Network Access",
                "Spacious & Versatile Electric SUV",
                "How Do I Charge My EV?",
                "No More Gas Stations",
                "Front-Load Fun with a Frunk"
            ],
            "descriptions": [
                "Leave range anxiety behind. The Mustang Mach-E with an available extended-range battery and RWD offers an impressive EPA-estimated range of up to 312 miles. Perfect for daily commutes, long road trips, and everything in between. Your next adventure has no limits.",
                "Charging your Mustang Mach-E is simple and convenient. Use the included Ford Mobile Power Cord for easy home charging, or install the available Ford Connected Charge Station for faster Level 2 charging. On the road, you get access to the BlueOval™ Charge Network, the largest public charging network in North America.",
                "Beyond its electric powertrain, the Mustang Mach-E is a versatile SUV designed for your life. It offers spacious seating for five, ample cargo room, and a drainable front trunk (frunk) for extra storage—perfect for groceries, gym bags, or even ice for a tailgate."
            ],
            "image_assets": [
                {
                    "asset_id": "img_301_charge",
                    "name": "mach_e_charging_at_home.jpg",
                    "alt_text": "A Mustang Mach-E plugged into a Ford Connected Charge Station in a modern garage.",
                    "description": "This image conveys the convenience and simplicity of home charging, showing the vehicle in a clean, aspirational residential setting. It addresses common questions about EV ownership logistics."
                },
                {
                    "asset_id": "img_302_frunk",
                    "name": "mach_e_frunk_with_groceries.jpg",
                    "alt_text": "The open front trunk (frunk) of a Mustang Mach-E filled with grocery bags.",
                    "description": "Highlights the practical, unexpected storage space of the Mach-E. This asset is useful for demonstrating the vehicle's versatility and everyday usability beyond just being a performance car."
                }
            ]
        }
    }

    return [performance_creative, technology_creative, practicality_creative]

@mcp.tool()
def get_campaign_ad_creatives(campaign_id: str) -> str:
    """
    Retrieves all ad creatives for a given campaign ID as a JSON string.
    This mock version returns a highly verbose set of creatives for a Ford Mustang Mach-E.

    Args:
        campaign_id: The ID of the campaign to fetch ad creatives for.

    Returns:
        A JSON string representing a list of ad creatives.
    """
    print(f"Received request for verbose Ford campaign_id: {campaign_id}")

    if not campaign_id or campaign_id.isspace():
        error_response = {
            "error": "Invalid campaign_id provided.",
            "message": "campaign_id cannot be empty."
        }
        return json.dumps(error_response, indent=2)

    mock_creatives = generate_ford_mach_e_creatives(campaign_id)

    # Convert the list of creatives to a JSON string with indentation for readability
    json_output = json.dumps(mock_creatives, indent=2)
    
    print(f"Returning {len(mock_creatives)} verbose ad creatives for campaign {campaign_id}.")
    return json_output

if __name__ == "__main__":
    print("Starting Mock Google Ads MCP Server with Verbose Ford Campaign Data...")
    print("Available tools: get_campaign_ad_creatives(campaign_id: str)")
    print("Server is expecting requests via the configured transport (e.g., stdio).")
    
    try:
        mcp.run(transport='stdio')
    except Exception as e:
        print(f"An error occurred during server run: {e}")

