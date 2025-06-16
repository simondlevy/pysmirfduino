void serialEvent1()
{
    if (Serial1.available()) {       
        Serial.write(Serial1.read()); 
    }
}

void setup() 
{
    Serial.begin(115200);
    Serial1.begin(115200);
}

void loop() 
{
    static uint8_t k;

    Serial1.write(97+k);
    Serial1.write(10);
    k = (k + 1) % 26;
}
