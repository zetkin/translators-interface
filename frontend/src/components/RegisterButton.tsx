import React, { useState, useContext } from 'react'
import { fade } from '@material-ui/core/styles'

import theme from '../../styles/theme'
import { UserEmailContext } from '../contexts/userEmailContext'

import RegisterDialog from './RegisterDialog'
import SignoutDialog from './SignoutDialog'

const RegisterButton = () => {
  const { userEmail } = useContext(UserEmailContext)
  const [registerDialogOpen, setRegisterDialogOpen] = useState(false)
  const [signoutDialogOpen, setSignoutDialogOpen] = useState(false)

  return (
    <>
      <button
        style={{
          cursor: 'pointer',
          backgroundColor: fade(theme.palette.common.white, 0.15),
          color: theme.palette.common.white,
          borderRadius: 4,
          padding: theme.spacing(1, 2),
          border: 'none',
        }}
        onClick={(e) => {
          // If user is signed in, show the signout dialog
          if (userEmail) setSignoutDialogOpen(true)
          // If user is not signed in, show the register dialog
          else setRegisterDialogOpen(true)
        }}
      >
        <span style={{ color: 'inherit', fontSize: '1.1em' }}>
          {userEmail || 'Enter your email'}
        </span>
      </button>
      <RegisterDialog
        open={registerDialogOpen}
        onClose={() => {
          setRegisterDialogOpen(false)
        }}
      />
      <SignoutDialog
        open={signoutDialogOpen}
        onClose={() => {
          setSignoutDialogOpen(false)
        }}
      />
    </>
  )
}

export default RegisterButton
