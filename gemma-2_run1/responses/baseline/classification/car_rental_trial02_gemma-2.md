| label | element | arg1 | arg2 |
|---|---|---|---|
| C | RentalLocation | | |
| C | BusinessModel | | |
| C | Customer | | |
| C | JobMarket | | |
| C | LaborCost | | |
| C | OperatingCost | | |
| C | BusinessOperation | | |
| C | ImprovementProposal | | |
| C | PassengerCar | | |
| C | VehicleRental | | |
| C | ReservationSystem | | |
| C | RentalFleet | | |
| C | Manufacturer | | |
| C | Model | | |
| C | PriceClass | | |
| C | Make | | |
| C | RentalPlan | | |
| C | DailyUnlimitedMilesPlan | | |
| C | Weekend10PercentDiscountPlan | | |
| C | Car | | |
| C | AutomaticGearChange | | |
| C | ManualGearChange | | |
| C | TwoDoors | | |
| C | FourDoors | | |
| C | Sedan | | |
| C | Hatchback | | |
| C | RentalPrice | | |
| C | Reservation | | |
| C | Salesperson | | |
| C | ReservationForm | | |
| C | FileCabinet | | |
| C | Deposit | | |
| C | Contract | | |
| C | Period | | |
| C | BlockReservation | | |
| C | Invoice | | |
| C | Rental | | |
| C | CreditCard | | |
| C | CreditCardProcessingCompany | | |
| C | PreventiveMaintenance | | |
| C | Damage | | |
| C | Disposal | | |
| C | Depreciation | | |
| A | name | RentalLocation | |
| A | type | BusinessModel | |
| A | target | BusinessModel | |
| A | rentalLocations | BusinessModel | |
| A | serviceQuality | BusinessModel | |
| A | customerSatisfaction | BusinessModel | |
| A | laborCost | LaborCost | |
| A | operatingCost | OperatingCost | |
| A | businessName | Business | |
| A | services | Business | |
| A | marketPosition | Business | |
| A | number | JobMarket | |
| A | demand | JobMarket | |
| A | supply | JobMarket | |
| A | vehicles | RentalFleet | |
| A | models | RentalFleet | |
| A | manufacturers | RentalFleet | |
| A | rentalPlans | RentalFleet | |
| A | priceClasses | RentalFleet | |
| A | rentalPrices | RentalFleet | |
| A | location | RentalLocation | |
| A | availableCars | RentalLocation | |
| A | reviews | RentalLocation | |
| A | customerCount | RentalLocation | |
| A | make | Car | |
| A | model | Car | |
| A | year | Car | |
| A | transmission | Car | |
| A | doors | Car | |
| A | fuelType | Car | |
| A | rentalPrice | Car | |
| A | description | Car | |
| A | rentalDuration | Rental | |
| A | pickUpDate | Rental | |
| A | returnDate | Rental | |
| A | totalCost | Rental | |
| A | customer | Rental | |
| A | car | Rental | |
| A | status | Rental | |
| A | paymentMethod | Rental | |
| A | depositAmount | Rental | |
| A | damageReport | Rental | |
| A | contract | Rental | |
| A | salespersons | Business | |
| A | form | ReservationForm | |
| A | customerInformation | ReservationForm | |
| A | carSelection | ReservationForm | |
| A | rentalDates | ReservationForm | |
| A | paymentDetails | ReservationForm | |
| A | status | Reservation | |
| A | confirmationNumber | Reservation | |
| A | amount | Invoice | |
| A | paymentDate | Invoice | |
| A | description | Invoice | |
| A | items | Invoice | |
| A | customerID | Invoice | |
| A | rentalID | Invoice | |
| A | creditCard | CreditCard | |
| A | cardNumber | CreditCard | |
| A | expiryDate | CreditCard | |
| A | cvv | CreditCard | |
| A | name | CreditCard | |
| A | companyName | CreditCardProcessingCompany | |
| A | processingFee | CreditCardProcessingCompany | |
| A | transactionID | CreditCardProcessingCompany | |
| A | maintenanceDate | Car | |
| A | mileage | Car | |
| A | damageHistory | Car | |
| A | disposalMethod | Car | |
| A | depreciationValue | Car | |
| AS | operates | Business | RentalLocation |
| AS | offers | Business | RentalPlan |
| AS | includes | RentalPlan | Car |
| AS | provides | Business | Customer |
| AS | processes | Business | Invoice |
| AS | processes | CreditCardProcessingCompany | CreditCard |
| AS | rents | RentalLocation | Car |
| AS | reserves | Customer | Car |
| AS | issues | Business | Invoice |
| AS | submits | Customer | ReservationForm |
| AS | generates | Business | Invoice |
| AS | processes | Business | Reservation |


