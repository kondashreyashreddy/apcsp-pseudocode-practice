num <- RANDOM(1,100)
ui <- 0

REPEAT UNTIL(ui = num)
{
    DISPLAY("Enter user guess: ")
    ui <- INPUT()
    IF(ui < num)
    {
        DISPLAY("Too Low")
        IF(ui < 1)
        {
            DISPLAY("Minimum Value is 1")
        }
    }
    ELSE
    {
        IF(ui > num)
        {
            DISPLAY("Too High")
            IF(ui > 100)
            {
                DISPLAY("Maximum Value is 100")
            }
        }
        ELSE
        {
            DISPLAY("You inputted the correct number!")
        }
    }
}
