class EXAMPLE_QUERIES:
    """
    Set of example queries for usage with GraphQL API functions.
    Mostly from https://github.com/Rhein-Neckar-Verkehr/Data-Hub-API-How-To
    """

    monitor = """query {
                    station(id: "2417") {
                      hafasID
                      longName
                      journeys(startTime: "2024-02-26T17:00:00Z", first: 2) {
                        totalCount
                        elements {
                          ... on Journey {
                            line {
                              id
                            }
                            stops(onlyHafasID: "2417") {
                              plannedDeparture {
                                isoString
                              }
                              realtimeDeparture {
                                isoString
                              }
                            }
                          }
                        }
                      }
                    }
                  }"""

    load = """query {
        station(id: "2417") {
          hafasID
          longName
          journeys(startTime: "2024-02-26T17:00:00Z", first: 3) {
            totalCount
            elements {
              ... on Journey {
                id
                line {
                  id
                }
                loadsForecastType

                loads(onlyHafasID: "2417") {
                  realtime
                  forecast
                  adjusted
                  loadType
                  ratio
                }

                stops(only: "2417") {
                  plannedDeparture {
                    isoString
                  }

                  realtimeDeparture {
                    isoString
                  }
                }
              }
            }
          }
        }
      }"""

    pagination = """query {
                      stations (first: 20, after: "1106") { # the value of the cursor is added here
                        totalCount
                        cursor
                        elements  {
                          ... on Station {
                            shortName
                          }
                        }
                      }
                    }"""

    station = """query {
                        station(id: "2471") {
                          hafasID
                          longName
                          shortName
                          name
                        }
                      }"""

    stations = """query{
                      stations(first: 3, lat: 49.483076, long: 8.468409, distance: 0.5) {
                        totalCount
                        cursor
                        elements {
                          ... on Station {
                            hafasID
                            globalID
                            longName
                            id
                          }
                        }
                      }
                    }"""

    trip = """query {
                trips(
                  originGlobalID: "de:08222:2471"
                  destinationGlobalID: "de:08222:2417"
                  departureTime: "2024-02-26T17:00:00Z"
                ) {
                  startTime {
                    isoString
                  }
        
                  endTime {
                    isoString
                  }
        
                  interchanges
        
                  legs {
                    ... on InterchangeLeg {
                      mode
                    }
        
                    ... on TimedLeg {
                      board {
                        point {
                          ... on StopPoint {
                            ref
                            stopPointName
                          }
                        }
                        estimatedTime {
                          isoString
                        }
                        timetabledTime {
                          isoString
                        }
                      }
        
                      alight {
                        point {
                          ... on StopPoint {
                            ref
                            stopPointName
                          }
                        }
        
                        estimatedTime {
                          isoString
                        }
                        timetabledTime {
                          isoString
                        }
                      }
        
                      service {
                        type
                        name
                        description
                        destinationLabel
                      }
                    }
        
                    ... on ContinuousLeg {
                      mode
                    }
                  }
                }
            }"""