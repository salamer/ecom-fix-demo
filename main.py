from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from typing import List, Optional
import json

app = FastAPI()

# Templates
templates = Jinja2Templates(directory="templates")

# Mock sneaker data - Gen-Z vibes
SNEAKERS = [
    {
        "id": 1,
        "name": "Air Flux Neon",
        "brand": "StreetVibe",
        "price": 149.99,
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500",
        "colors": ["Neon Green", "Electric Blue", "Hot Pink"],
        "sizes": [7, 8, 9, 10, 11, 12],
        "description": "Turn heads with these electric colorways. Perfect for late-night city adventures.",
        "rating": 4.8,
        "reviews": 234,
        "category": "Lifestyle",
        "trending": True
    },
    {
        "id": 2,
        "name": "Cyber Runner X",
        "brand": "FutureFeet",
        "price": 189.99,
        "image": "https://images.unsplash.com/photo-1605348532760-6753d2c43329?w=500",
        "colors": ["Chrome Silver", "Matte Black", "Holographic"],
        "sizes": [7, 8, 9, 10, 11, 12],
        "description": "Cyberpunk meets comfort. These kicks are straight from 2077.",
        "rating": 4.9,
        "reviews": 567,
        "category": "Performance",
        "trending": True
    },
    {
        "id": 3,
        "name": "Retro Wave 95",
        "brand": "VaporWave",
        "price": 129.99,
        "image": "https://images.unsplash.com/photo-1600185365926-3a2ce3cdb9eb?w=500",
        "colors": ["Purple Haze", "Sunset Orange", "Teal Dream"],
        "sizes": [6, 7, 8, 9, 10, 11],
        "description": "90s nostalgia with modern comfort. Aesthetic overload guaranteed.",
        "rating": 4.7,
        "reviews": 189,
        "category": "Retro",
        "trending": False
    },
    {
        "id": 4,
        "name": "Cloud Walker",
        "brand": "SkyStep",
        "price": 159.99,
        "image": "https://images.unsplash.com/photo-1549298916-b41d501d3772?w=500",
        "colors": ["Pure White", "Sky Blue", "Lavender"],
        "sizes": [7, 8, 9, 10, 11, 12],
        "description": "Walk on clouds. Literally the softest sneakers you'll ever wear.",
        "rating": 4.9,
        "reviews": 423,
        "category": "Comfort",
        "trending": True
    },
    {
        "id": 5,
        "name": "Urban Jungle Pro",
        "brand": "StreetVibe",
        "price": 169.99,
        "image": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=500",
        "colors": ["Camo Green", "Tiger Orange", "Snake Print"],
        "sizes": [7, 8, 9, 10, 11, 12, 13],
        "description": "Survive the concrete jungle in style. Built tough, looks tougher.",
        "rating": 4.6,
        "reviews": 312,
        "category": "Lifestyle",
        "trending": False
    },
    {
        "id": 6,
        "name": "Glow Up Premium",
        "brand": "LuxeKicks",
        "price": 199.99,
        "image": "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=500",
        "colors": ["Rose Gold", "Pearl White", "Champagne"],
        "sizes": [6, 7, 8, 9, 10, 11],
        "description": "For when you need to flex. Premium materials, premium vibes only.",
        "rating": 4.8,
        "reviews": 678,
        "category": "Premium",
        "trending": True
    },
    {
        "id": 7,
        "name": "Speed Demon",
        "brand": "FutureFeet",
        "price": 174.99,
        "image": "https://images.unsplash.com/photo-1551107696-a4b0c5a0d9a2?w=500",
        "colors": ["Racing Red", "Carbon Black", "Velocity Yellow"],
        "sizes": [7, 8, 9, 10, 11, 12],
        "description": "Built for speed. Feel the rush every time you lace up.",
        "rating": 4.7,
        "reviews": 445,
        "category": "Performance",
        "trending": False
    },
    {
        "id": 8,
        "name": "Pastel Dreams",
        "brand": "SoftStep",
        "price": 139.99,
        "image": "https://images.unsplash.com/photo-1600269452121-4f2416e55c28?w=500",
        "colors": ["Baby Pink", "Mint Green", "Soft Yellow"],
        "sizes": [6, 7, 8, 9, 10, 11],
        "description": "Soft aesthetics, soft comfort. Perfect for your feed and your feet.",
        "rating": 4.8,
        "reviews": 523,
        "category": "Lifestyle",
        "trending": True
    }
]

# API Routes
@app.get("/api/products")
async def get_products(category: Optional[str] = None, trending: Optional[bool] = None):
    """Get all products with optional filters"""
    filtered = SNEAKERS

    if category:
        filtered = [s for s in filtered if s["category"].lower() == category.lower()]

    if trending is not None:
        filtered = [s for s in filtered if s["trending"] == trending]

    return JSONResponse(content=filtered)

@app.get("/api/products/{product_id}")
async def get_product(product_id: int):
    """Get single product by ID"""
    product = next((s for s in SNEAKERS if s["id"] == product_id), None)
    if product:
        return JSONResponse(content=product)
    return JSONResponse(content={"error": "Product not found"}, status_code=404)

@app.get("/api/categories")
async def get_categories():
    """Get all unique categories"""
    categories = list(set(s["category"] for s in SNEAKERS))
    return JSONResponse(content=categories)

# Frontend Routes
@app.get("/")
async def home(request: Request):
    """Homepage with all sneakers"""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "sneakers": SNEAKERS,
        "page_title": "SneakPeak - Fresh Kicks for Gen-Z"
    })

@app.get("/product/{product_id}")
async def product_detail(request: Request, product_id: int):
    """Product detail page"""
    product = next((s for s in SNEAKERS if s["id"] == product_id), None)
    if not produc:
      return JSONResponse(content={"error": "Product not found"}, status_code=404)
    return templates.TemplateResponse("product.html", {
        "request": request,
        "product": product,
        "page_title": f"{product['name']} - SneakPeak"
    })

@app.get("/checkout")
async def checkout(request: Request):
    """Checkout page"""
    return templates.TemplateResponse("checkout.html", {
        "request": request,
        "page_title": "Checkout - SneakPeak"
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
