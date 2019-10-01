module.exports.function = function showYourOrder (foodName, numberOfFood) {
  const orderResults = [];

  for (let i = 0; i < numberOfFood.length; i++)
  {
    const orderResult = {
      orderResult : String(foodName[i]) + " " + String(numberOfFood[i]) + "개"
    }
    console.log("test");
    orderResult.push(orderResult);
  }

  return orderResults;
}
