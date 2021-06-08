import React, { createContext, useEffect, useState } from 'react'

import { USER_EMAIL_LOCAL_STORAGE_KEY } from '../constants'

export const UserEmailContext = createContext({
  userEmail: undefined,
  setUserEmail: undefined,
})

export const UserEmailProvider = ({ children }) => {
  const [userEmail, setUserEmail] = useState(
    process.browser
      ? window.localStorage.getItem(USER_EMAIL_LOCAL_STORAGE_KEY)
      : undefined
  )

  // Listens to changes to set userEmail and updates LocalStorage when changed
  useEffect(() => {
    if (userEmail != null)
      localStorage.setItem(USER_EMAIL_LOCAL_STORAGE_KEY, userEmail)
    else localStorage.removeItem(USER_EMAIL_LOCAL_STORAGE_KEY)
  }, [userEmail])

  return (
    <UserEmailContext.Provider value={{ userEmail, setUserEmail }}>
      {children}
    </UserEmailContext.Provider>
  )
}
