dictionary = {
    "App_Dev_Frontend": {
        # "Web": {
        #     "React.js": {
        #         "State Management: Redux / Redux Toolkit (RTK)": {
        #             "API Client: TanStack Query": {"End of Flow": "Technology stack selected"},
        #             "API Client: Axios": {"End of Flow": "Technology stack selected"},
        #             "API Client: Fetch API": {"End of Flow": "Technology stack selected"}
        #         },
        #         "State Management: Zustand": {
        #             "API Client: TanStack Query": {"End of Flow": "Technology stack selected"},
        #             "API Client: Axios": {"End of Flow": "Technology stack selected"},
        #             "API Client: Fetch API": {"End of Flow": "Technology stack selected"}
        #         },
        #         "State Management: React Context API (Built-in)": {
        #             "API Client: TanStack Query": {"End of Flow": "Technology stack selected"},
        #             "API Client: Axios": {"End of Flow": "Technology stack selected"},
        #             "API Client: Fetch API": {"End of Flow": "Technology stack selected"}
        #         }
        #     },
        #     "Vue.js": {
        #         "State Management: Pinia": {
        #             "API Client: Axios": {"End of Flow": "Technology stack selected"},
        #             "API Client: Fetch API": {"End of Flow": "Technology stack selected"}
        #         },
        #         "State Management: Vuex (Legacy)": {
        #             "API Client: Axios": {"End of Flow": "Technology stack selected"},
        #             "API Client: Fetch API": {"End of Flow": "Technology stack selected"}
        #         }
        #     },
        #     "Angular": {
        #         "State Management: NgRx": {
        #             "API Client: RxJS Services (Built-in)": {"End of Flow": "Technology stack selected"}
        #         },
        #         "State Management: RxJS Services (Built-in)": {
        #             "API Client: RxJS Services (Built-in)": {"End of Flow": "Technology stack selected"}
        #         }
        #     },
        #     "Svelte": {
        #         "State Management: Svelte Stores (Built-in)": {
        #             "API Client: Axios": {"End of Flow": "Technology stack selected"},
        #             "API Client: Fetch API": {"End of Flow": "Technology stack selected"}
        #         }
        #     }
        # },
        "Mobile": {
            "Native iOS (Swift)": {
                "Framework: SwiftUI": {
                    "State Management: Combine": {
                        "API Client: URLSession": {"End of Flow": "Technology stack selected"},
                        "API Client: Alamofire": {"End of Flow": "Technology stack selected"}
                    }
                },
                "Framework: UIKit": {
                    "State Management: Closures/Delegates": {
                        "API Client: URLSession": {"End of Flow": "Technology stack selected"},
                        "API Client: Alamofire": {"End of Flow": "Technology stack selected"}
                    }
                }
            },
            "Native Android (Kotlin)": {
                "Framework: Jetpack Compose": {
                    "State Management: ViewModel with StateFlow": {
                        "API Client: Retrofit": {"End of Flow": "Technology stack selected"},
                        "API Client: Ktor Client": {"End of Flow": "Technology stack selected"}
                    }
                },
                 "Framework: XML": {
                    "State Management: ViewModel with LiveData": {
                        "API Client: Retrofit": {"End of Flow": "Technology stack selected"},
                        "API Client: Ktor Client": {"End of Flow": "Technology stack selected"}
                    }
                }
            },
            "React Native (JS/TS)": {
                "State Management: Redux / Redux Toolkit (RTK)": {
                    "API Client: Axios": {"End of Flow": "Technology stack selected"},
                    "API Client: Fetch API": {"End of Flow": "Technology stack selected"}
                },
                "State Management: Zustand": {
                    "API Client: Axios": {"End of Flow": "Technology stack selected"},
                    "API Client: Fetch API": {"End of Flow": "Technology stack selected"}
                }
            }
        },
        "Desktop": {
            "Electron (JS/TS)": {
                "UI Framework: React.js": {
                    "State Management: Redux Toolkit": {
                       "API Client: Fetch API / Axios": {"End of Flow": "Technology stack selected"}
                    }
                },
                "UI Framework: Vue.js": {
                     "State Management: Pinia": {
                       "API Client: Fetch API / Axios": {"End of Flow": "Technology stack selected"}
                    }
                }
            },
            "Tauri (Rust + JS/TS)": {
                "UI Framework: React.js": {
                    "State Management: Zustand": {
                        "API Client: Tauri API / Fetch": {"End of Flow": "Technology stack selected"}
                    }
                },
                "UI Framework: Svelte": {
                    "State Management: Svelte Stores": {
                        "API Client: Tauri API / Fetch": {"End of Flow": "Technology stack selected"}
                    }
                }
            }
        },
        "Cross-Platform (Mobile + Desktop)": {
            "Flutter (Dart)": {
                "State Management: BLoC / Cubit": {
                    "API Client: Dio": {"End of Flow": "Technology stack selected"},
                    "API Client: http": {"End of Flow": "Technology stack selected"}
                },
                "State Management: Riverpod": {
                    "API Client: Dio": {"End of Flow": "Technology stack selected"},
                    "API Client: http": {"End of Flow": "Technology stack selected"}
                }
            },
            ".NET MAUI (C#)": {
                "State Management: MVVM Pattern": {
                    "API Client: HttpClient": {"End of Flow": "Technology stack selected"},
                    "API Client: Refit": {"End of Flow": "Technology stack selected"}
                }
            }
        }
    },
    "App_Dev_Backend": {
        "JavaScript / TypeScript (Node.js)": {
            "Express.js": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"},
                "gRPC": {"End of Flow": "Technology stack selected"},
                "WebSocket": {"End of Flow": "Technology stack selected"}
            },
            "NestJS": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"},
                "gRPC": {"End of Flow": "Technology stack selected"},
                "WebSocket": {"End of Flow": "Technology stack selected"}
            },
            "Fastify": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"},
                "gRPC": {"End of Flow": "Technology stack selected"},
                "WebSocket": {"End of Flow": "Technology stack selected"}
            },
            "Koa.js": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"},
                "gRPC": {"End of Flow": "Technology stack selected"},
                "WebSocket": {"End of Flow": "Technology stack selected"}
            },
            "AdonisJS": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"},
                "gRPC": {"End of Flow": "Technology stack selected"},
                "WebSocket": {"End of Flow": "Technology stack selected"}
            }
        },
        "Python": {
            "Django": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"},
                "WebSocket": {"End of Flow": "Technology stack selected"}
            },
            "Flask": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"},
                "WebSocket": {"End of Flow": "Technology stack selected"}
            },
            "FastAPI": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"},
                "WebSocket": {"End of Flow": "Technology stack selected"}
            },
            "Tornado": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"},
                "WebSocket": {"End of Flow": "Technology stack selected"}
            }
        },
        "Java": {
            "Spring Boot": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"},
                "gRPC": {"End of Flow": "Technology stack selected"},
                "SOAP": {"End of Flow": "Technology stack selected"}
            },
            "Quarkus": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"},
                "gRPC": {"End of Flow": "Technology stack selected"},
                "SOAP": {"End of Flow": "Technology stack selected"}
            },
            "Micronaut": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"},
                "gRPC": {"End of Flow": "Technology stack selected"},
                "SOAP": {"End of Flow": "Technology stack selected"}
            },
            "Jakarta EE": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"},
                "gRPC": {"End of Flow": "Technology stack selected"},
                "SOAP": {"End of Flow": "Technology stack selected"}
            }
        },
        "C# (.NET)": {
            "ASP.NET Core": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"},
                "gRPC": {"End of Flow": "Technology stack selected"},
                "SignalR": {"End of Flow": "Technology stack selected"}
            }
        },
        "Go (Golang)": {
            "net/http (Standard Library)": {
                "REST": {"End of Flow": "Technology stack selected"},
                "gRPC": {"End of Flow": "Technology stack selected"}
            },
            "Gin": {
                "REST": {"End of Flow": "Technology stack selected"},
                "gRPC": {"End of Flow": "Technology stack selected"}
            },
            "Echo": {
                "REST": {"End of Flow": "Technology stack selected"},
                "gRPC": {"End of Flow": "Technology stack selected"}
            },
            "Chi": {
                "REST": {"End of Flow": "Technology stack selected"},
                "gRPC": {"End of Flow": "Technology stack selected"}
            }
        },
        "PHP": {
            "Laravel": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"}
            },
            "Symfony": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"}
            },
            "Slim": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"}
            }
        },
        "Ruby": {
            "Ruby on Rails": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"}
            },
            "Sinatra": {
                "REST": {"End of Flow": "Technology stack selected"},
                "GraphQL": {"End of Flow": "Technology stack selected"}
            }
        }
    }
}

def traverse_dict(dictionary):
    current_dict = dictionary
    while True:
        # ---- NEW LOGIC: Auto-skip levels with only one choice ----
        while len(current_dict) == 1 and isinstance(list(current_dict.values())[0], dict):
            single_key = list(current_dict.keys())[0]
            print(f"--> Auto-selecting the only option: '{single_key}'")
            current_dict = current_dict[single_key]
        # -----------------------------------------------------------

        # After auto-skipping, present the multiple choices or the final leaf
        options = list(current_dict.keys())
        print("\nPlease choose from the following options:")
        print('\n'.join(f"- {key}" for key in options))

        key = input("\nEnter your choice, or 'exit' to quit: ")

        if key.lower() == 'exit':
            break

        if key in current_dict:
            next_level = current_dict[key]
            if isinstance(next_level, dict):
                current_dict = next_level
            else:
                # This is a leaf node (the final value)
                print(f"\n✅ Leaf Node Reached! Value: {next_level}")
                print("--- Restarting from the top ---\n")
                current_dict = dictionary
        else:
            print("\n❌ Invalid key. Please try again.")


# Start the traversal
traverse_dict(dictionary)