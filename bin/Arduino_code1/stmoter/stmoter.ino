#include <Stepper.h>


const int stepstep = 4;

Stepper
sstep(stepstep, 11, 9, 10, 8);
void setup()
{
  Serial.begin(9600);
  sstep.setSpeed(1800);
}

void loop()
{
  while (Serial.available() > 0)
  {
    char c = Serial.read();
    if( c == 'y')
    {
        sstep.step(stepstep);
        delay(0);
    }
    else if( c == 'n')
    {
        sstep.step(-stepstep);
        delay(0);
    }
  }
}
