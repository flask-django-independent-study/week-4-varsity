const displayError = document.getElementById('displayError')
const displayMessage = document.getElementById('displayMessage')

const openAccount = document.getElementById('openAccount')
const viewAccount = document.getElementById('viewAccount')
const closeAccount = document.getElementById('closeAccount')

const openAccountForm = document.getElementById('openAccountForm')
const viewAccountForm = document.getElementById('viewAccountForm')
const closeAccountForm = document.getElementById('closeAccountForm')

const openAccountConfirm = document.getElementById('openAccountConfirm')
const viewAccountConfirm = document.getElementById('viewAccountConfirm')
const closeAccountConfirm = document.getElementById('closeAccountConfirm')

const displayAccount = document.getElementById('displayAccount')
const displayAccountHolder = document.getElementById('displayAccountHolder')
const displayAccountBalance = document.getElementById('displayAccountBalance')
const deposit = document.getElementById('deposit')
const withdraw = document.getElementById('withdraw')

const displayDeposit = document.getElementById('displayDeposit')
const displayDepositHolder = document.getElementById('displayDepositHolder')
const depositConfirm = document.getElementById('depositConfirm')

const displayWithdraw = document.getElementById('displayWithdraw')
const displayWithdrawHolder = document.getElementById('displayWithdrawHolder')
const withdrawConfirm = document.getElementById('withdrawConfirm')

const closeAllForms = () => {
  openAccountForm.style.display = 'none'
  viewAccountForm.style.display = 'none'
  closeAccountForm.style.display = 'none'
}

const clearRightSide = () => {
  closeAllForms()
  displayError.style.display = 'none'
  displayMessage.style.display = 'none'
  displayAccount.style.display = 'none'
  displayDeposit.style.display = 'none'
  displayWithdraw.style.display = 'none'
}

const showDisplayAccount = (holder, balance) => {
  displayAccount.style.display = 'block'
  displayAccountHolder.innerHTML = holder
  displayAccountBalance.innerHTML = balance
}

const showDisplayError = error => {
  displayError.style.display = 'block'
  displayError.innerHTML = error
}

const showDisplayMessage = message => {
  displayMessage.style.display = 'block'
  displayMessage.innerHTML = message
}

openAccount.addEventListener('click', () => {
  clearRightSide()
  openAccountForm.style.display = 'block'
})

viewAccount.addEventListener('click', () => {
  clearRightSide()
  viewAccountForm.style.display = 'block'
})

deposit.addEventListener('click', () => {
  const holder = displayAccountHolder.innerHTML
  clearRightSide()
  displayDeposit.style.display = 'block'
  displayDepositHolder.innerHTML = holder
})

withdraw.addEventListener('click', () => {
  const holder = displayAccountHolder.innerHTML
  clearRightSide()
  displayWithdraw.style.display = 'block'
  displayWithdrawHolder.innerHTML = holder
})

closeAccount.addEventListener('click', () => {
  clearRightSide()
  closeAccountForm.style.display = 'block'
})

// Here is an example of an axios call. On openAccountConfirm which is the
// button to open an account on the right half of the screen (you can look
// into the "home.html.j2" to see the button with this id), we set a click
// listener. When the button is clied we get the account holder by accessing
// openAccountHolder. We then call post on axios, pass in the url (api endpoint),
// then as a second argument, pass in any data we want to send with the post
// request. In this case, we want to send holder with the accountHolder.value
// The backend is expecting this json data "holder".

// Upon a successful response we set the accountHolder.value to '', we
// close all forms and then we check for which data we got back. If the
// reponse.data.error is returned we display that by passing in the data to
// the function showDisplayError, else we pass the data into the function
// showDisplayMessage.

// Upon an unsuccessful response we catch it and console.log the error. Please
// note the error we received in the response.data is not the same as when we
// catch an error. The response.data.error is json data that is purposely sent
// from the backend to display a user friendly error. The error in the catch
// block will be displayed in the event that we have a server error or the data
// we sent to the back end was not in the correct format.

// NOTE: in the post request we did not need to "jsonify" the data. This is
// because JSON stands for JavaScript Object Notation. The curly braces in js
// are already JSON.

openAccountConfirm.addEventListener('click', () => {
  const accountHolder = document.getElementById('openAccountHolder')
  axios.post('/api/account', {
    holder: accountHolder.value
  }).then(response => {
    accountHolder.value = ''
    closeAllForms()
    if (response.data.error) {
      showDisplayError(response.data.error)
    } else {
      showDisplayMessage(response.data.message)
    }
  }).catch(error => {
    console.log(error)
  })
})

viewAccountConfirm.addEventListener('click', () => {
  const accountHolder = document.getElementById('viewAccountHolder')
  // TODO: add an axios get request to get an account for a given holder
  // HINT: check out the html to understand what's going on.
  // HINT: checkout showDisplayError and showDisplayAccount functions
})

// TODO: be sure to test these buttons as we go to avoid testing everything at
// the end

depositConfirm.addEventListener('click', () => {
  const accountHolder = document.getElementById('displayDepositHolder').innerHTML
  const amount = document.getElementById('depositAmount')
  // TODO: add an axios post request to deposit to an account with the given
  // holder and amount
})

withdrawConfirm.addEventListener('click', () => {
  const accountHolder = document.getElementById('displayWithdrawHolder').innerHTML
  const amount = document.getElementById('withdrawAmount')
  // TODO: add an axios post request to withdraw to an account with the given
  // holder and amount
})

closeAccountConfirm.addEventListener('click', () => {
  const accountHolder = document.getElementById('closeAccountHolder')
  // TODO: add an axios delete request to close an account with the given holder
})
