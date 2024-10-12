//package main
//
//import (
//	"bytes"
//	"encoding/json"
//	"fmt"
//	"net/http"
//	"time"
//)
//
//const (
//	brazeAPIKey   = "658f43d7-c5f0-462a-959d-6288a4bd4918"
//	brazeEndpoint = "https://rest.iad-07.braze.com/campaigns/list"
//	segmentID     = "YOUR_SEGMENT_ID"
//)
//
//type SchedulePayload struct {
//	ApiKey    string      `json:"api_key"`
//	Messages  interface{} `json:"messages"`
//	SegmentID string      `json:"segment_id"`
//	Schedule  Schedule    `json:"schedule"`
//}
//
//type Schedule struct {
//	Time string `json:"time"`
//}
//
//func schedulePushNotification(timeToSend string) error {
//	payload := SchedulePayload{
//		ApiKey:    brazeAPIKey,
//		SegmentID: segmentID,
//		Schedule:  Schedule{Time: timeToSend},
//		Messages: map[string]interface{}{
//			"push": map[string]interface{}{
//				"alert": "This is a scheduled push notification",
//			},
//		},
//	}
//
//	body, err := json.Marshal(payload)
//	if err != nil {
//		return err
//	}
//
//	req, err := http.NewRequest("POST", brazeEndpoint, bytes.NewBuffer(body))
//	if err != nil {
//		return err
//	}
//
//	req.Header.Set("Content-Type", "application/json")
//
//	client := &http.Client{Timeout: time.Second * 10}
//	resp, err := client.Do(req)
//	if err != nil {
//		return err
//	}
//
//	defer resp.Body.Close()
//	fmt.Printf("Response status: %s\n", resp.Status)
//	return nil
//}
//
//func main() {
//	err := schedulePushNotification("2024-09-30T09:00:00")
//	if err != nil {
//		fmt.Printf("Error scheduling push notification at 8 AM: %v\n", err)
//	}
//
//	err = schedulePushNotification("2024-09-30T18:00:00")
//	if err != nil {
//		fmt.Printf("Error scheduling push notification at 6 PM: %v\n", err)
//	}
//}

package main

//import (
//	"fmt"
//	"io/ioutil"
//	"log"
//	"net/http"
//)
//
//const (
//	brazeAPIKey   = "658f43d7-c5f0-462a-959d-6288a4bd4918"
//	brazeEndpoint = "https://rest.iad-07.braze.com/campaigns/list"
//)
//
////	brazeAPIKey   = "658f43d7-c5f0-462a-959d-6288a4bd4918"
////	brazeEndpoint = "https://rest.iad-07.braze.com/campaigns/list"
//
//func fetchCampaignDetails(campaignID string) {
//	url := fmt.Sprintf("%s?campaign_id=%s", brazeEndpoint, campaignID)
//
//	req, err := http.NewRequest("GET", url, nil)
//	if err != nil {
//		log.Fatalf("Error creating GET request: %v", err)
//	}
//
//	req.Header.Set("Authorization", fmt.Sprintf("Bearer %s", brazeAPIKey))
//
//	client := &http.Client{}
//	resp, err := client.Do(req)
//	if err != nil {
//		log.Fatalf("Error making GET request: %v", err)
//	}
//	defer resp.Body.Close()
//
//	body, err := ioutil.ReadAll(resp.Body)
//	if err != nil {
//		fmt.Println("Error creating GET request")
//		log.Fatalf("Error reading response body: %v", err)
//	}
//
//	fmt.Printf("Response: %s\n", body)
//}
//
//func main() {
//	fetchCampaignDetails("your_campaign_id_here")
//}
