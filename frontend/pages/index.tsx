import { GetStaticProps, NextPage } from 'next'
import Head from 'next/head'
import NextLink from 'next/link'

import {
  Container,
  Typography,
  Box,
  Card,
  Link,
  CardContent,
  Chip,
  CardHeader,
} from '@material-ui/core'

import { Project } from '../src/global.types'
import { getProjects } from '../src/api/projects'

/**
 * Home Page - Lists Projects
 */

interface StaticProps {
  projects: Project[]
}

export const getStaticProps: GetStaticProps<StaticProps> = async () => {
  const projects = await getProjects()
  return { props: { projects } }
}

const Home: NextPage<StaticProps> = ({ projects }) => {
  return (
    <div>
      <Head>
        <title>Zetkin Translators Interface</title>
        <meta
          name="description"
          content="Contribute to the localisation of Zetkin's software"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <Container style={{ marginTop: 40, marginBottom: 20 }}>
          <Typography variant="h3" component="h1" style={{ marginBottom: 40 }}>
            Projects
          </Typography>

          <div
            style={{
              display: 'grid',
              gridTemplateColumns: '1fr 1fr 1fr',
              gridTemplateRows: 'auto',
              alignItems: 'center',
              gridGap: 20,
            }}
          >
            {/* Projects */}
            {projects.map((project) => {
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
                              label={language.name}
                              style={{ marginRight: 5 }}
                            ></Chip>
                          </NextLink>
                        )
                      })}
                    </Box>
                  </Card>
                </NextLink>
              )
            })}
          </div>
        </Container>
      </main>
    </div>
  )
}

export default Home
