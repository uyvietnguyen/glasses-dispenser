const getGlasses = (rightPrescription, leftPrescription) => {
  fetch('https://localhost:3000', {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      firstParam: 'yourValue',
      secondParam: 'yourOtherValue',
    }),
  });
};

export { getGlasses };
