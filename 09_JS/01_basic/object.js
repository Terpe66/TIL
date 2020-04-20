const me = {
    name: "우너",
    "phone number": "01012341234",
    appleProducts: {
        ipad: "2018pro",
        iphone: "6s+",
        macbook: "2018pro"
    }
};

me.name; // 우너
me["name"]; // 우너
me["phone number"]; // 01012341234
me.appleProducts; // { ipad: ... }
me.appleProducts.ipad; // 2018pro
