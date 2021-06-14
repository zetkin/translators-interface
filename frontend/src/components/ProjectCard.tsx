import React, { useState, useContext } from 'react'
import { fade } from '@material-ui/core/styles'
import { Card, Box, Typography, Link, Chip } from '@material-ui/core'

import NextLink from 'next/link'
import dayjs from 'dayjs'
import relativeTime from 'dayjs/plugin/relativeTime'

import { EN_LANGUAGE_CODE, COUNTRIES } from '../constants'
import { Project } from '../global.types'

dayjs.extend(relativeTime)

interface Props {
  project: Project
}

const ProjectCard = ({ project }: Props) => {
  const lastSyncTime = dayjs(project.last_sync_time)
  const timeFromLastSync = lastSyncTime.isValid()
    ? dayjs(new Date()).to(lastSyncTime)
    : null

  return (
    <NextLink
      href={{
        pathname: '/projects/[id]',
        query: { id: project.id },
      }}
    >
      <Card
        key={project.id}
        style={{
          padding: 20,
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
          cursor: 'pointer',
        }}
      >
        <Box>
          <Typography gutterBottom variant="h6" component="h4">
            {project.name}
          </Typography>
          <Typography gutterBottom component="p">
            {timeFromLastSync
              ? ` Last synced ${timeFromLastSync}`
              : `Not yet synced`}
          </Typography>
          <Typography gutterBottom component="p">
            <Link
              onClick={(e) => {
                e.stopPropagation()
              }}
              href={`https://www.github.com/${project.repository_name}`}
            >
              {project.repository_name}
            </Link>
          </Typography>
        </Box>

        <Box display="flex" style={{ marginTop: 20 }}>
          {project.languages.map((language) => {
            if (language.language_code !== EN_LANGUAGE_CODE) {
              const country = COUNTRIES[language.language_code]

              return (
                <NextLink
                  href={{
                    pathname: '/projects/[id]/[language_code]',
                    query: {
                      id: project.id,
                      language_code: language.language_code,
                    },
                  }}
                >
                  <Chip
                    label={`${country?.flag || ''} ${language.name}`}
                    style={{
                      marginRight: 5,
                      color: 'white',
                      backgroundColor: country
                        ? fade(
                            COUNTRIES[language.language_code]?.color ||
                              'inherit',
                            0.6
                          )
                        : 'grey',
                    }}
                  ></Chip>
                </NextLink>
              )
            }
            return null
          })}
        </Box>
      </Card>
    </NextLink>
  )
}

export default ProjectCard
