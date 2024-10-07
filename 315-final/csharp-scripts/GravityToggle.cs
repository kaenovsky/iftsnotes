using UnityEngine;

public class GravityToggle : MonoBehaviour
{
    private bool isGravityOn = true;

    // Additional parameters for rotation and force
    public float upwardForce = 0.0003f; // Adjust this as needed for a gentle lift
    public float spinTorque = 0.003f; // A small amount of torque

    // Method to toggle gravity
    public void ToggleGravity()
{
    // Find all objects tagged as "Ball" and "Cup"
    GameObject[] balls = GameObject.FindGameObjectsWithTag("Ball");
    GameObject[] cups = GameObject.FindGameObjectsWithTag("Cup");

    // Toggle gravity for balls
    foreach (GameObject ball in balls)
    {
        Rigidbody rb = ball.GetComponent<Rigidbody>();
        if (rb != null)
        {
            rb.useGravity = isGravityOn; // Toggle gravity
            rb.velocity = Vector3.zero; // Reset velocity to avoid unexpected movement
            
            // Apply a small upward force and a spin
            if (!isGravityOn) // Only apply when turning gravity off
            {
                rb.AddForce(Vector3.up * upwardForce, ForceMode.Impulse); // Apply upward force
                rb.AddTorque(Random.insideUnitSphere * spinTorque, ForceMode.Impulse); // Apply random spin
            }
        }
    }

    // Toggle gravity for cups
    foreach (GameObject cup in cups)
    {
        Rigidbody rb = cup.GetComponent<Rigidbody>();
        if (rb != null)
        {
            rb.useGravity = isGravityOn; // Toggle gravity
            rb.velocity = Vector3.zero; // Reset velocity to avoid unexpected movement
            
            // Apply a small upward force and a spin
            if (!isGravityOn) // Only apply when turning gravity off
            {
                rb.AddForce(Vector3.up * upwardForce, ForceMode.Impulse); // Apply upward force
                rb.AddTorque(Random.insideUnitSphere * spinTorque, ForceMode.Impulse); // Apply random spin
            }
        }
    }

    // Toggle the gravity state
    isGravityOn = !isGravityOn;
}
}